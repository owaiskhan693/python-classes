# Python Functions
# a function is a block of reusable code that performs a specific task
def display():
    print("python programming")

display()
display()



def say_name():
    print("hello python")

say_name()


def fruits():
    print("apple")
    print("mango")
    print("banana")
    print("orange")

fruits()

def names():
    print("Owais")
    print("zain")
    print("junaid")

names()


def languages():
    print("Pashto")
    print("Urdu")
    print("balochi")

languages()


def city():
    print("karachi")

city()

def study():
    print("Python")
    print("VS Code")
    print("Practice")

study()
study()

# function with parameter and function with arguments mixed practice
# place parameter 
# karachi arguments


def city(place):
    print(place)

city("karachi")


def student(name, age):
    print(name)
    print(age)


student("owais", 16)

def add(a, b):
    print(a + b)

add(10, 10)


def employee(emp_name, city, salary):
    print(emp_name)
    print(city)
    print(salary)

employee("Owais", "Karachi", 50000)


def school(name, class_name, section):
    print(name)
    print(class_name)
    print(section)

school("Owais", "9th", "A")


def car(brand):
    print(brand)

car("toyota")


def mobile(company):
    print(company)

mobile("iphone")


def market(name):
    print(name)

market("bolden market")


def rectangle(length, width):
    print(length)
    print(width)

rectangle(5, 3)

def marks(english, science, math):
    print(english)
    print(science)
    print(math)

marks(95, 90, 88)


# positional arguments
# positional arguments are arguments that are matched to parameters by their position (order)

def student(name, age):
    print(name)
    print(age)

student("Owais", 16)

def add(a, b):
    print(a + b)

add(50, 60)

def subtract(a, b):
    print(a - b)

subtract(40, 18)


def country(name, capital):
    print(name)
    print(capital)

country("Afghanistan", "Kabul")

def multiply(a, b):
    print(a * b)

multiply(4, 4)

def divide(a, b):
    print(a/b)

divide(2, 4)


def is_even( x ):
    if x % 2 == 0:
        return True
    else:
        return False
    
greet = is_even(20)
if (greet):
    print("Number is even")
else:
    print("Number is odd")


# default argument
# a default argument is a parameter that has a default value if no argument is passed the default value is used
def lesson(name="Owais"):
    print(name)

lesson()

def greet(fruit_name="apple"):
    print(fruit_name)

greet("banana")

def mobile_company(name="sumsung"):
    print(name)

mobile_company("infinix")


def add(a=10, b=5):
    print(a + b)

add(20)


def subtract(a=4, b=3):
    print(a - b)

subtract(80, 69)


def company(name="toyoto"):
    print(name)

company()


def market(name="saddar"):
    print(name)

market("bolden market")


def info(name="Owais", age=16, salary=50000, city="karachi"):
    print(name)
    print(age)
    print(salary)
    print(city)
info(salary=80000, city="Peshawar")


def info(name="Owais", salary=50000, department="IT"):
    print(name)
    print(salary)
    print(department)

info(salary=80000, department="HR")


def marks(islamiat=98, urdu=95, english=86):
    print(islamiat + urdu + english)

marks(english=91)


def marks(islamiat=98, urdu=95, english=86):
    print(islamiat + urdu + english)

marks()



def marks(islamiat=98, urdu=95, english=86):
    print(islamiat + urdu + english)

marks(100, 90, 62)


def rectangle(length=15, width=3):
    print(length * width)

rectangle()

def rectangle(length=45, height=30, breadth=20):
    print(length - height - breadth)

rectangle()

def rectangle(length=18, height=10, breadth=7,):
    print(length + height + breadth)

rectangle(50, 80, 60)


def rectangle(length=5, width=2):
    print(length / width)

rectangle()


def employee(name="Owais", age=16, city="Karachi", salary=50000, department="IT"):
    print(name)
    print(age)
    print(city)
    print(salary)
    print(department)

employee(city="Peshawar", salary=100000)


def laptop(brand="Dell", ram=8, storage=512, color="Black", price=100000):
    print(brand)
    print(ram)
    print(storage)
    print(color)
    print(price)

laptop()


def laptop(brand="Dell", ram=8, storage=512, color="Black", price=100000):
    print(brand)
    print(ram)
    print(storage)
    print(color)
    print(price)

laptop("HP", 16, 1024, price=110000)


def school(name="Owais", class_name="9th", section="A", marks=490, city="Peshawar"):
    print(name)
    print(class_name)
    print(section)
    print(marks)
    print(city)

school()


def school(name="Owais", class_name="9th", section="A", marks=490, city="Peshawar"):
    print(name)
    print(class_name)
    print(section)
    print(marks)
    print(city)

school("junaid", "10th", "C", 498)


def table(num=4):
    for i in range(1,11):
        print(num, "x", i, "=", num * i)

table()


def countdown(start=1):
    for i in range(start, 0, -10):
        print(i)

countdown()

def countdown(start=20):
    for i in range(start, 0, -1):
        print(i)

countdown(30)

def stars(rows=5):
    for i in range(rows):
        print("*")

stars()






































































































































































































































