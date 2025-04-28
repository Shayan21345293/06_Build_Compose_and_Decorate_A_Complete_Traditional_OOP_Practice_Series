# 1. Using self
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

student1 = Student("Ali", 85)
student1.display()


# 2. Using cls
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")

c1 = Counter()
c2 = Counter()
Counter.display_count()


# 3. Public Variables and Methods
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} car is starting.")

car1 = Car("Toyota")
print(car1.brand)
car1.start()


# 4. Class Variables and Class Methods
class Bank:
    bank_name = "State Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

b1 = Bank()
b2 = Bank()
print(Bank.bank_name)
Bank.change_bank_name("National Bank")
print(b1.bank_name)
print(b2.bank_name)


# 5. Static Variables and Static Methods
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(3, 7))


# 6. Constructors and Destructors
class Logger:
    def __init__(self):
        print("Logger object created.")

    def __del__(self):
        print("Logger object destroyed.")

logger1 = Logger()
del logger1


# 7. Access Modifiers: Public, Private, and Protected
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # public
        self._salary = salary     # protected
        self.__ssn = ssn           # private

emp = Employee("John", 50000, "123-45-6789")
print(emp.name)           # accessible
print(emp._salary)        # accessible but should be treated as protected
# print(emp.__ssn)        # not directly accessible
print(emp._Employee__ssn)  # name mangling


# 8. The super() Function
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

teacher1 = Teacher("Sara", "Math")
print(teacher1.name, teacher1.subject)


# 9. Abstract Classes and Methods
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(5, 4)
print(rect.area())


# 10. Instance Methods
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking!")

dog1 = Dog("Rocky", "Bulldog")
dog1.bark()


# 11. Class Methods
class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

Book.increment_book_count()
Book.increment_book_count()
print(Book.total_books)


# 12. Static Methods
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

print(TemperatureConverter.celsius_to_fahrenheit(0))


# 13. Composition
class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_engine(self):
        self.engine.start()

engine1 = Engine()
car1 = Car(engine1)
car1.start_engine()


# 14. Aggregation
class Department:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee

class Employee:
    def __init__(self, name):
        self.name = name

emp1 = Employee("Ali")
dept1 = Department("HR", emp1)
print(dept1.employee.name)


# 15. Method Resolution Order (MRO) and Diamond Inheritance
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

d = D()
d.show()  # Follows MRO


# 16. Function Decorators
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

say_hello()


# 17. Class Decorators
def add_greeting(cls):
    class NewClass(cls):
        def greet(self):
            return "Hello from Decorator!"
    return NewClass

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Ali")
print(p.greet())


# 18. Property Decorators: @property, @setter, and @deleter
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            print("Invalid price!")

    @price.deleter
    def price(self):
        del self._price

product = Product(100)
print(product.price)
product.price = 200
print(product.price)
del product.price


# 19. callable() and __call__()
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return self.factor * number

m = Multiplier(5)
print(callable(m))
print(m(3))


# 20. Creating a Custom Exception
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older.")

try:
    check_age(16)
except InvalidAgeError as e:
    print(e)


# 21. Make a Custom Class Iterable
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < 0:
            raise StopIteration
        current = self.start
        self.start -= 1
        return current

for num in Countdown(5):
    print(num)

