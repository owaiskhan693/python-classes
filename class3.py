# python if else
x = 45
if x > 45:
    print("x is less than 45")
    print("Its in if")
    print("double if")
    print("triple if")
else:
    print("x is not less than 45" )
    print("else")
print("end")



x = int(input("enter your marks"))

if x % 2 == 0:
    print("{x} is the even number")
else:
    print("{x} is the odd number")





x = int(input("Please enter  marks"))


if x > 85:
    print("grade A")
    age = int(input("whats your age"))
    if age > 18:
        print("Awesome! you are very young")
    else:
        print("Good")
elif x > 70:
     print("grade B")
elif x > 60:
    print("grade C")
elif x > 50:
    print("grade D")

    

# short hand if 
x = 10
if x < 10 : print("x is less than 10")


# short hand if else (conditional statement)
x = 8
if x < 8:
    print("x is less than 8")
else:
    print("x is not less than 8")
    
print("x is less than 8") if x < 8 else print("x is not less than 8")


# while loop

x = 2

print("Before While")

while x <= 7:
        print(x)
        x = x + 1

print("After While")






x = 1

print("Before While")

while x <= 100:
    if x % 2 == 0:
        print(x)
    x = x + 1

print("After While")


x = 2

print("Before While")

while x <= 7:
        print(x)
        x = x + 1
else:
     print("in else while")

print("After While")
print(x)


s1 = "Python Programming"

l= len(s1)
x = 0
while x < 1:
     print(s1[x])
     x = x + 1

print("Exit")



s1 = "Python Programming"

l = len(s1)
x = 0
while x < 1:
     if s1[x] not in 'aeiou':
        print(s1[x])   
     x = x + 1

print("Exist")






# vowels not print concept

text = "hello world"
vowels = "aeiou"

i = 0

while i < len(text):
     if text[i] not in vowels:
          print(text[i])
     i += 1






