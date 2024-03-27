from abc import ABC, abstractmethod


class LogMixin:
    def __repr__(self):
        attrs = ', '.join([f"{attr}={value}" for attr, value in self.__dict__.items()])
        return f"{self.__class__.__name__}({attrs})"


class AbstractProduct(ABC):
    @abstractmethod
    def __init__(self, title, description, price, quantity):
        self.title = title
        self.description = description
        self._price = float(price)
        self.quantity = int(quantity)

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price):
        pass

    @abstractmethod
    def __str__(self):
        pass


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
        if isinstance(product, AbstractProduct):
            self.__goods.append(product)
            Category.total_unique_products += 1
        else:
            raise TypeError("Можно добавлять только продукты или их наследников в категорию")

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


class Product(AbstractProduct, LogMixin):
    def __init__(self, title, description, price, quantity):
        super().__init__(title, description, price, quantity)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self._price = float(new_price)
        else:
            print("Цена введена некорректно!")

    def __str__(self):
        return f"{self.title}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Складывать продукты разных классов нельзя")
        if isinstance(other, AbstractProduct):
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError("Error: неизвестный тип объекта")


class Smartphone(AbstractProduct, LogMixin):
    def __init__(self, title, description, price, quantity, performance, model, memory_capacity, color):
        super().__init__(title, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory_capacity = memory_capacity
        self.color = color

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self._price = float(new_price)
        else:
            print("Цена введена некорректно!")

    def __str__(self):
        return f"{super().__str__()}, Производительность: {self.performance}, Модель: {self.model}, Объем памяти: {self.memory_capacity}, Цвет: {self.color}"


class LawnGrass(AbstractProduct, LogMixin):
    def __init__(self, title, description, price, quantity, country_of_origin, germination_period, color):
        super().__init__(title, description, price, quantity)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self._price = float(new_price)
        else:
            print("Цена введена некорректно!")

    def __str__(self):
        return f"{super().__str__()}, Страна-производитель: {self.country_of_origin}, Срок прорастания: {self.germination_period}, Цвет: {self.color}"
