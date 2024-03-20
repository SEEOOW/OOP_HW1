class Category:
    total_categories = 0
    total_unique_products = 0

    def __init__(self, title, description, products=None):
        self.title = title
        self.description = description
        if products is None:
            products = []
        self.__goods = list(set(products))
        Category.total_categories += 1
        Category.total_unique_products += len(self.__goods)

    def add_product(self, product):
        self.__goods.append(product)
        Category.total_unique_products += 1

    @property
    def goods(self):
        return self.__goods

    def display_list_products(self):
        result = ''
        for product in self.__goods:
            result += f'{product}\n'
        return result

    def __len__(self):
        return len(self.__goods)

    def __str__(self):
        return f"{self.title}, количество продуктов: {len(self)} шт."


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
    def create(cls, **kwargs):
        new_product = cls(**kwargs)
        return new_product

    def __str__(self):
        return f"{self.title}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError("Unsupported operand type(s) for +: 'Product' and '{}'".format(type(other)))


class Smartphone(Product):
    def __init__(self, title, description, price, quantity, performance, model, memory_capacity, color):
        super().__init__(title, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory_capacity = memory_capacity
        self.color = color

    def __str__(self):
        return f"{super().__str__()}, Производительность: {self.performance}, Модель: {self.model}, Объем памяти: {self.memory_capacity}, Цвет: {self.color}"


class LawnGrass(Product):
    def __init__(self, title, description, price, quantity, country_of_origin, germination_period, color):
        super().__init__(title, description, price, quantity)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        return f"{super().__str__()}, Страна-производитель: {self.country_of_origin}, Срок прорастания: {self.germination_period}, Цвет: {self.color}"
