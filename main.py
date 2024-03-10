class Category:
    total_categories = 0
    total_unique_products = 0

    def __init__(self, title, description):
        self.title = title
        self.description = description
        self._goods = []  # сделать список товаров приватным атрибутом
        Category.total_categories += 1

# метод добавления товаров
    def add_products(self, product):
        self._goods.append(product)
        Category.total_unique_products += 1

# Для атрибута класса Category «товары» добавить геттер
    @property
    def display_list_products(self):
        result = ''
        for product in self._goods:
            result += f'{product.title}, {product.price} руб. Остаток: {product.quantity} шт.'
        return result


class Product:
    def __init__(self, title, description, price, quantity):
        self.title = title
        self.description = description
        self._price = float(price)
        self.quantity = int(quantity)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self._price = float(new_price)
        else:
            print("Цена введена некорректно!")

    @classmethod
    def create_product(cls, title, description, price, quantity):
        new_product = cls(title, description, price, quantity)
        return new_product
