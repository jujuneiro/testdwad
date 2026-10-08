import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QTableWidgetItem,
    QHeaderView, QWidget, QLabel
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

from ui_login import Ui_MainWindow as Login
from ui_autorazation import Ui_MainWindow as Auto
from ui_cart import Ui_CartDialog as Cart
from database import authenticate_user, get_all_categories, get_all_products, create_order


class CartWindow(QWidget):
    """Окно просмотра корзины и оформления заказа"""
    def __init__(self, user_info, cart_items, parent_catalog):
        super().__init__()
        self.ui = Cart()
        self.ui.setupUi(self)
       
        self.user_info = user_info
        self.cart_items = cart_items
        self.parent_catalog = parent_catalog

        self.setup_ui()

    def setup_ui(self):
        self.ui.backButton.clicked.connect(self.close)
        self.ui.clearCartButton.clicked.connect(self.clear_cart)
        self.ui.removeItemButton.clicked.connect(self.remove_selected_item)
        self.ui.checkoutButton.clicked.connect(self.process_checkout)

        self.refresh_table()

    def refresh_table(self):
        headers = ["ID", "Наименование", "Цена (руб.)", "Кол-во", "Сумма (руб.)"]
        self.ui.cartTable.setColumnCount(len(headers))
        self.ui.cartTable.setHorizontalHeaderLabels(headers)
        self.ui.cartTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.cartTable.setRowCount(0)

        total_sum = 0.0

        for row_idx, item in enumerate(self.cart_items):
            # item = [product_id, name, price, qty, sum]
            self.ui.cartTable.insertRow(row_idx)
            item_sum = item[2] * item[3]
            item[4] = item_sum
            total_sum += item_sum

            self.ui.cartTable.setItem(row_idx, 0, QTableWidgetItem(str(item[0])))
            self.ui.cartTable.setItem(row_idx, 1, QTableWidgetItem(str(item[1])))
            self.ui.cartTable.setItem(row_idx, 2, QTableWidgetItem(f"{item[2]:.2f}"))
            self.ui.cartTable.setItem(row_idx, 3, QTableWidgetItem(str(item[3])))
            self.ui.cartTable.setItem(row_idx, 4, QTableWidgetItem(f"{item_sum:.2f}"))

        self.ui.totalPriceLabel.setText(f"Итого к оплате: {total_sum:,.2f} руб.".replace(",", " "))
        self.total_sum = total_sum

    def remove_selected_item(self):
        current_row = self.ui.cartTable.currentRow()
        if current_row >= 0:
            self.cart_items.pop(current_row)
            self.refresh_table()
        else:
            QMessageBox.warning(self, "Внимание", "Выберите строку для удаления!")

    def clear_cart(self):
        self.cart_items.clear()
        self.refresh_table()

    def process_checkout(self):
        if not self.cart_items:
            QMessageBox.warning(self, "Ошибка", "Корзина пуста!")
            return

        fio = self.user_info.get("fio", "Анонимный клиент")
        if create_order(fio, self.cart_items, self.total_sum):
            QMessageBox.information(self, "Успех", "Заказ успешно оформлен!")
            self.cart_items.clear()
            self.parent_catalog.cart = []
            self.close()
        else:
            QMessageBox.critical(self, "Ошибка", "Не удалось сохранить заказ в БД.")


class AutoReraz(QMainWindow):
    """Окно каталога товаров"""
    def __init__(self, user_info):
        super().__init__()
        self.ui = Auto()
        self.ui.setupUi(self)
       
        self.user_info = user_info
        self.all_products = []
        self.cart = []  # Корзина хранит элементы [p_id, name, price, qty, sum]

        self.setup_ui_logic()
        self.apply_role_permissions()
        self.init_catalog_data()

    def setup_ui_logic(self):
        fio = self.user_info.get("fio", "Гость")
        role = self.user_info.get("role_name", "Неавторизованный")
        self.ui.userinfolabel.setText(f"{fio} ({role})")
       
        self.ui.LogoutButton.clicked.connect(self.logout)
        self.ui.addToOrderButton.clicked.connect(self.handle_add_to_order)

        self.ui.searchLineEdit.textChanged.connect(self.apply_filters)
        self.ui.filterComboBox.currentTextChanged.connect(self.apply_filters)
        self.ui.sortComboBox.currentIndexChanged.connect(self.apply_filters)

    def handle_add_to_order(self):
        """Добавление выделенного товара в корзину и открытие окна корзины"""
        current_row = self.ui.productsTable.currentRow()
       
        # Если товар выделен в таблице — добавляем его
        if current_row >= 0:
            image_label = self.ui.productsTable.cellWidget(current_row, 0)
            product_id = int(image_label.property("product_id"))
            product_name = self.ui.productsTable.item(current_row, 1).text()
            price_text = self.ui.productsTable.item(current_row, 6).text().replace(" ", "").replace(",", ".")
            price = float(price_text)

            # Проверяем, есть ли товар уже в корзине
            found = False
            for item in self.cart:
                if item[0] == product_id:
                    item[3] += 1  # Увеличиваем количество
                    found = True
                    break

            if not found:
                self.cart.append([product_id, product_name, price, 1, price])

        # Открываем окно корзины
        self.cart_window = CartWindow(self.user_info, self.cart, self)
        self.cart_window.show()

    def apply_role_permissions(self):
        role_id = self.user_info.get("role_id", 0)

        if role_id == 0:  # Гость
            self.ui.addToOrderButton.hide()
            self.ui.manageOrdersButton.hide()
        elif role_id == 1:  # Пользователь
            self.ui.addToOrderButton.show()
            self.ui.manageOrdersButton.hide()
        elif role_id in [2, 3]:  # Менеджер и Админ
            self.ui.addToOrderButton.show()
            self.ui.manageOrdersButton.show()

    def init_catalog_data(self):
        headers = ["Фото", "Наименование", "Категория", "Подкатегория", "Производитель", "Состав", "Цена (руб.)", "Остаток"]
        self.ui.productsTable.setColumnCount(len(headers))
        self.ui.productsTable.setHorizontalHeaderLabels(headers)
        self.ui.productsTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.ui.sortComboBox.clear()
        self.ui.sortComboBox.addItems(["Без сортировки", "Сначала дешевые", "Сначала дорогие"])

        self.ui.filterComboBox.clear()
        self.ui.filterComboBox.addItem("Все категории")
        categories = get_all_categories()
        self.ui.filterComboBox.addItems(categories)

        self.all_products = get_all_products()
        self.apply_filters()

    def apply_filters(self):
        search_text = self.ui.searchLineEdit.text().lower().strip()
        selected_category = self.ui.filterComboBox.currentText()
        sort_index = self.ui.sortComboBox.currentIndex()

        filtered = []

        for p in self.all_products:
            p_id, name, cat, subcat, manuf, comp, price, qty = p

            if search_text and not (search_text in name.lower() or search_text in manuf.lower()):
                continue

            if selected_category != "Все категории" and cat != selected_category:
                continue

            filtered.append(p)

        if sort_index == 1:
            filtered.sort(key=lambda x: x[6])
        elif sort_index == 2:
            filtered.sort(key=lambda x: x[6], reverse=True)

        self.display_products(filtered)

    def display_products(self, products):
        self.ui.productsTable.setRowCount(0)

        for row_idx, product in enumerate(products):
            self.ui.productsTable.insertRow(row_idx)

            p_id, name, cat, subcat, manuf, comp, price, qty = product

            # =========================
            # КАРТИНКА ТОВАРА
            # =========================
            image_label = QLabel()
            image_label.setAlignment(Qt.AlignCenter)

            # Картинки лежат в images/boots и называются 1.jpg, 2.jpg ... 31.jpg
            image_path = f"images/{p_id}.png"
            pixmap = QPixmap(image_path)

            if not pixmap.isNull():
                pixmap = pixmap.scaled(
                    100,
                    100,
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
                image_label.setPixmap(pixmap)
            else:
                image_label.setText("Нет фото")

            # Сохраняем ID товара внутри QLabel,
            # чтобы корзина продолжала работать
            image_label.setProperty("product_id", p_id)

            self.ui.productsTable.setCellWidget(
                row_idx,
                0,
                image_label
            )

            # =========================
            # ОСТАЛЬНЫЕ ДАННЫЕ ТОВАРА
            # =========================
            values = [
                name,
                cat,
                subcat,
                manuf,
                comp,
                price,
                qty
            ]

            for col_idx, value in enumerate(values, start=1):
                if col_idx == 6:
                    item_text = f"{value:,.2f}".replace(",", " ")
                else:
                    item_text = str(value)

                item = QTableWidgetItem(item_text)
                item.setFlags(item.flags() ^ Qt.ItemIsEditable)

                if col_idx in [6, 7]:
                    item.setTextAlignment(
                        Qt.AlignRight | Qt.AlignVCenter
                    )

                self.ui.productsTable.setItem(
                    row_idx,
                    col_idx,
                    item
                )

            # Высота строки под картинку
            self.ui.productsTable.setRowHeight(row_idx, 110)

    def logout(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()


class LoginWindow(QMainWindow):
    """Окно авторизации"""
    def __init__(self):
        super().__init__()
        self.ui = Login()
        self.ui.setupUi(self)

        self.ui.loginButton.clicked.connect(self.handle_login)
        self.ui.guestButton.clicked.connect(self.handle_guest_login)

    def handle_login(self):
        login = self.ui.loginLineEdit_2.text().strip()
        if not login:
            QMessageBox.warning(self, "Ошибка", "Введите логин!")
            return

        user_info = authenticate_user(login)

        if user_info:
            self.open_catalog(user_info)
        else:
            QMessageBox.critical(self, "Ошибка", "Пользователь не найден!")

    def handle_guest_login(self):
        guest_info = {
            "fio": "Гость",
            "role_name": "Неавторизованный пользователь",
            "role_id": 0
        }
        self.open_catalog(guest_info)

    def open_catalog(self, user_info):
        self.catalog = AutoReraz(user_info)
        self.catalog.show()
        self.close()


def main():
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()