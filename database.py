import psycopg2

DB_CONFIG = {
    "dbname": "local",
    "user": "postgres",
    "password": "12345678",
    "host": "localhost",
    "port": "5432"
}

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

def authenticate_user(login):
    """Авторизация пользователя по логину"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            SELECT u.last_name, u.first_name, u.patronymic, r.role_name, r.role_id
            FROM users u
            JOIN roles r ON u.role_id = r.role_id
            WHERE u.login = %s;
        """
        cursor.execute(query, (login,))
        user_data = cursor.fetchone()
        cursor.close()
        conn.close()

        if user_data:
            last_name, first_name, patronymic, role_name, role_id = user_data
            fio = f"{last_name} {first_name[0]}." if first_name else last_name
            if patronymic:
                fio += f"{patronymic[0]}."
            return {"fio": fio, "role_name": role_name, "role_id": role_id}
        return None
    except Exception as e:
        print(f"Ошибка БД (авторизация): {e}")
        return None

def get_all_categories():
    """Получение списка категорий для ComboBox"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT category_name FROM categories ORDER BY category_name;")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [r[0] for r in rows if r[0]]
    except Exception as e:
        print(f"Ошибка БД (категории): {e}")
        return []

def get_all_products():
    """Получение списка всех товаров со связями и остатками"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            SELECT
                p.product_id,
                p.product_name,
                COALESCE(c.category_name, 'Не указана') AS category_name,
                COALESCE(s.subcategory_name, '—') AS subcategory_name,
                COALESCE(m.manufacturer_name, 'Не указан') AS manufacturer_name,
                COALESCE(p.composition, '—') AS composition,
                p.price,
                COALESCE(SUM(st.quantity_available), 0) AS total_quantity
            FROM products p
            LEFT JOIN subcategories s ON p.subcategory_id = s.subcategory_id
            LEFT JOIN categories c ON s.category_id = c.category_id
            LEFT JOIN manufacturers m ON p.manufacturer_id = m.manufacturer_id
            LEFT JOIN stock_items st ON p.product_id = st.product_id
            GROUP BY
                p.product_id, p.product_name, c.category_name,
                s.subcategory_name, m.manufacturer_name, p.composition, p.price
            ORDER BY p.product_id;
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    except Exception as e:
        print(f"Ошибка БД (товары): {e}")
        return []

def create_order(user_fio, cart_items, total_price):
    """
    Сохранение заказа в PostgreSQL.
    cart_items: список [product_id, name, price, quantity, sum]
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()
       
        # 1. Создаем запись в таблице orders
        query_order = """
            INSERT INTO orders (order_date, client_fio, total_amount)
            VALUES (CURRENT_DATE, %s, %s)
            RETURNING order_id;
        """
        cursor.execute(query_order, (user_fio, total_price))
        order_id = cursor.fetchone()[0]

        # 2. Добавляем позиции заказа в order_items
        query_item = """
            INSERT INTO order_items (order_id, product_id, quantity, price_per_unit)
            VALUES (%s, %s, %s, %s);
        """
        for item in cart_items:
            p_id, _, price, qty, _ = item
            cursor.execute(query_item, (order_id, p_id, qty, price))

        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(f"Ошибка сохранения заказа: {e}")
        return False
