# arbitary arguments (*args)
# arbitary arguments allows a function to accept any number of arguments it is written with * before the parameter name

def greet(*fruits):
    print(fruits)

greet("apple", "banana", "mango", "orange", "grapes", "pine apple", "water milon")

def marks(*data):
    print(data)

marks("math",80,"english", 85, "urdu", 96)

def marks(*args):
    for i in args:
        print(i)

marks("math",80,"english", 85, "urdu", 96, "science", 78, "islamiat", 100)

# indexing in function type arbitary arguments *args
def numbers(a, b, c, *greet):
    print(a)
    print(b)
    print(c)
    print(greet)
    print(greet[0])

numbers(500, 300, 200, 20, 50, 80, 100, 10, 5)


def result(*data):
    for i in data:
        print(i)

result(
    "Urdu = 95",
    "Math = 79",
    "Physics = 86",
    "Chemistry = 72",
    "Islamiat = 99",
    "English = 90",
    "Computer = 93"
)

def shopping(*data):
    for i in data:
        print(i)

shopping("Rice", "Oil", "Sugar", "Tea", "Milk", )

def family(*args):
    for member in args:
        print(member)

family("Grand Father", "Grand Mother", "Father", "Mother", "Brother", "Sister")


def cities(a,b,*args):
    print(a)
    print(b)
    print(args)

cities("Peshawar", "Quetta", "Karachi", "Rawalpindi", "Sialkot")


# keyword arbitary argument
# **kwargs allows a function to accept any number of keyword arguments python stores them in a dictionary
def numbers(a, b, c, **data):
    print(a)
    print(b)
    print(c)
    print(data)
    print(data["name"])
    print(data["city"])

numbers(a=500, b=300, c=200, name="Owais", age=16, city="karachi", x=10, y=5)


def student(**details):
    for key, value in details.items( ):
        print(key, "=", value)

student(name="Owais", class_name="9th", age=16, city="Peshawar")


def result(**marks):
    for subject, mark in marks.items( ):
        print(subject, "=", mark)

result(Math=90, English=85, Urdu=95, Physics=88, Chemistry=80)

