# dictionary type practice 
# a dictionary is a collection of data stored in key-value pairs

student = {
    "name": "owais",
    "age": 16,
    "city": "karachi"
}

# print(student)
# print(type(student))
# print(len(student))


person = {
    "name": "Owais",
    "age": 16,
    "country": "Pakistan",
    "city": "karachi",
    "village": "Buner"
}


print(person)
# data access
print(person["country"])
# value change
person["city"]= "Peshawar"
print(person)
# new key add in dictionary
person["salary"]= 30000
print(person)
# for loop use in dictionary
for x in person:
    print(x, person[x])
# items used to define key and value 
for key, value in person.items( ):
    print(key, value)

# dictionary functions
# 1 keys
# returns all keys of the dictionary
print(person.keys( ))
# 2 values
# returns all values of the dictionary
print(person.values( ))
# 3 items
# returns keys and values together
print(person.items( ))
# 4 get
# returns the value of the specified key
print(person.get("village"))
# 5 update
# update or adds key-value pairs
person.update({"name": "Owais khan"})
print(person)
# 6 pop
# removes a specified key
person.pop("country")
print(person)
# 7 clear
# removes all items
person.clear()
print(person)
# 8 copy
# created a copy of the dictionary
student = {
    "name": "owais",
    "age": 16,
    "city": "karachi"
}
new_student = student.copy( )
print(new_student)
# 9 popitem
# removes the last inserted item
student.popitem()
print(student)
# 10 setdefault
# returns value of key if key does not exist, it adds the key
student.setdefault("country", "Pakistan")
print(student)

# in operator used
print("city" in student)
print("age" in student)

# only keys print
for key in student:
    print(key)

# only values print
for value in student.values():
    print(value)

# from keys
# created a new dictionary with specified keys and same value
keys = ("1", "2", "3")
a =dict.fromkeys(keys, "Owais")
print(a)
# del keyword
del student["country"]
print(student)
# empty dictionary
student = { }
print(student)

# constructor dict
# dict is used to create a dictionary
student = dict(
    name = "owais",
    age = 16,
    city = "karachi"
)
print(student)

student = dict(name = "owais",
age = 16)
print(student)


car = dict([
    ("brand", "toyota"),
    ("year", 2026)
])
print(car)


student = dict(name="Owais", city= "karachi")
print(student)


employee = dict([
    ("name", "owais"),
    ("age", 16),
    ("work", "manager"),
    ("salary", 100000)
])
print(employee)


# dictionary comprehension
# dictionary comprehension is a short and easy way to create a dictionary using a loop
numbers = {x: x*2 for x in
range(1,10)}
print(numbers)

Students = {
    "Student1": {
        "Name": "Owais",
        "Age": 116,
        "City": "Peshawar",
    },
    "Student2": {
        "Name": "Junaid",
        "Age": 17,
        "City": "Karachi"
    },
    "Student3": {
        "Name": "Zain",
        "Age": 17,
        "City": "Quetta"
    }
}
print(Students["Student1"]["Name"])


# dictionary of list
student = {
    "name": "Owais",
    "subjects": ["math","urdu", "english"]
}
print(student["subjects"])




