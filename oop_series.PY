# 1. Using self:

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Student Name: {self.name}, Marks: {self.marks}")


student1 = Student("John", 90)
student1.display()


# 2. Using cls:

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")

obj1 = Counter()
obj2 = Counter()
Counter.display_count()

# 3. Public Variables and Methods:

class Car:
    brand = "Toyota"

    def start(self):
        print(f"{self.brand} car started.")

# Instantiate and access
car1 = Car()
print(car1.brand)
car1.start()

# 4. Class Variables and Class Methods:

class Bank:
    bank_name = "XYZ Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

# Change and display bank name
Bank.change_bank_name("ABC Bank")
print(Bank.bank_name)


# 5. Static Variables and Static Methods:

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Use static method
result = MathUtils.add(5, 3)
print(result)

# 6. Constructors and Destructors:

class Logger:
    def __init__(self):
        print("Object created!")

    def __del__(self):
        print("Object destroyed!")

# Create and delete object
obj = Logger()
del obj

# 7. Access Modifiers: Public, Private, and Protected:

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public
        self._salary = salary     # Protected
        self.__ssn = ssn         # Private

# Instantiate and access
emp = Employee("John", 50000, "123-45-6789")
print(emp.name)
print(emp._salary)

# 8. The super() Function:

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

# Instantiate Teacher
teacher = Teacher("John", "Math")
print(teacher.name)
print(teacher.subject)

# 9. Abstract Classes and Methods:

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

# Instantiate and calculate area
rect = Rectangle(5, 3)
print(rect.area())

# 10. Instance Methods:

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking!")

# Create dog and make it bark
dog = Dog("Buddy", "Golden Retriever")
dog.bark()

# 11. Class Methods:

class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Add new books
Book.increment_book_count()
Book.increment_book_count()
print(Book.total_books)

# 12. Static Methods:

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Convert Celsius to Fahrenheit
print(TemperatureConverter.celsius_to_fahrenheit(25))

# 13. Composition:

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_car(self):
        self.engine.start()

# Create objects
engine = Engine()
car = Car(engine)
car.start_car()

# 14. Aggregation:

class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, employee):
        self.employee = employee

# Create objects
emp = Employee("John")
dept = Department(emp)
print(dept.employee.name)

# 15. MRO and Diamond Inheritance:

class A:
    def show(self):
        print("Class A show()")

class B(A):
    def show(self):
        print("Class B show()")

class C(A):
    def show(self):
        print("Class C show()")

class D(B, C):
    pass

d = D()
d.show()  

# 16. Function Decorators:

def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

# Call function
say_hello()

# 17. Class Decorators:

def add_greeting(cls):
    cls.greet = lambda self: "Hello from Decorator!"
    return cls

@add_greeting
class Person:
    pass

# Call greet method
person = Person()
print(person.greet())

# 18. Property Decorators:

class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

# Instantiate and use property
product = Product(100)
print(product.price)
product.price = 120
print(product.price)
del product.price

# 19. __call__() Method:

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, num):
        return num * self.factor

# Use callable
multiplier = Multiplier(5)
print(callable(multiplier))
print(multiplier(4))

# 20. Creating a Custom Exception:

class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")

try:
    check_age(16)
except InvalidAgeError as e:
    print(e)

# 21. Making a Custom Class Iterable:

class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current

# Iterate through Countdown
countdown = Countdown(5)
for number in countdown:
    print(number)