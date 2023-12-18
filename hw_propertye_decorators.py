#1
class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value < 0:
            raise ValueError("Length must be a non-negative number")
        self._length = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("Width must be a non-negative number")
        self._width = value

    @property
    def area(self):
        return self._length * self._width

    def __repr__(self):
        return f"Rectangle(length={self._length}, width={self._width})"

    def __str__(self):
        return f"Rectangle: Length={self._length}, Width={self._width}, Area={self.area}"

rectangle = Rectangle(5, 10)
print(rectangle)  
print(rectangle.area)  

rectangle.length = 8
print(rectangle)  
####################################################

#2
class DiscountLimit:
    def __init__(self, limit):
        self.limit = limit
        self._value = None

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if value > self.limit:
            raise ValueError(f"Discount cannot exceed the limit of {self.limit}%")
        self._value = value

    def __delete__(self, instance):
        del self._value

class Product:
    discount = DiscountLimit(limit=20)

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discounted_price(self):
        if self.discount:
            discount_amount = self.price * (self.discount / 100)
            return self.price - discount_amount
        else:
            return self.price


product = Product("Laptop", 1000)

product.discount = 15
print(product.discounted_price())  


try:
    product.discount = 25  # ValueError
except ValueError as e:
    print(e)  # "Discount cannot exceed the limit of 20%"


print(product.discount) 