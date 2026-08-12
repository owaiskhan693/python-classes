# OOP (Object Oriented Programming)
# OOP is a programming style where we create "Objects" that have data and functions together, to model real-world things.
# class = blueprint
# object = Instance
# Data + Method = Attribute + Function

# four pillars of OOP
# Encapsulation
# Inheritance
# Polymorphism
# Abstraction

class Biryani:
    def __init__(self, chawal, gosht):
        self.chawal = chawal
        self.gosht = gosht
    def pakao(self):
        print(f"{self.chawal} aur {self.gosht} wali biryani pak rahi hai")

b1 = Biryani("basmati","chiken")
b2 = Biryani("seela", "beef")

b1.pakao()
b2.pakao()
    


class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} woof woof")

d1 = Dog("Tommy")
d1.bark()




