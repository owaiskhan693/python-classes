# Python List
# There are 4 types of built in data types used to store collections of data :
# 1 list
# 2 Tuple 
# 3 Set
# 4 Dictionary

# List
# Lists are used store multiple items in a single variable.  Lists are created using square brackets:


fruits = ['apple', 'banana', 'mango']
print(fruits)
print(type(fruits))


fruits = ['apple', 'banana', 'mango']
print(fruits[0])




fruits = ['apple', 'banana', 'mango']
fruits. append("orange")
print(fruits)




fruits = ["apple", "banana", "mango"]
fruits[1] = "orange"

print(fruits)





fruits = ["apple","banana","mango"]
fruits.remove("apple")

print(fruits)




fruits = ["apple", "banana", "mango"]
print(len(fruits))



fruits = ['apple', 'banana', 'mango']

for fruits in fruits:
    print(fruits)



colors = ["red", "green", "blue"]
print(colors[2])



numbers = [10, 20, 30, 40]
print(numbers[1])




names = ["ahmed", "zain", "junaid"]

names[1] = "owais"
print(names)




fruits = ["apple", "banana"]

fruits.append("mango")

print(fruits)



numbers = [10, 20, 30, 40]
numbers.remove(20)

print(numbers)



animals = ["cat", "dog"]
animals.append("cow")
animals.remove("cat")

print(animals)



names = ["ahmed", "zain", "junaid"]

print(len(names))


# slicing in list
fruits_names = ["apple", "banana", "mango", "cherry", "grapes"]
print(fruits_names[1:4])

print(len(fruits_names))
print(type(fruits_names))




# list constructor
# marks [180, 200, 250, 130, 100, 300]
marks = list( (180, 200, 250, 130, 100, 300) )
print(marks)


print("mango" in fruits_names)



# append method add the item in the last
fruits_names.append("pine apple")
print(fruits_names)




# insert method add an item at a specified index
fruits_names.insert(2,"water milon")
print(fruits_names)




# remove method remove any item 
fruits_names.remove("grapes")
print(fruits_names)




# pop method removes the last item
fruits_names.pop()
print(fruits_names)



# for loop and while loop used in list
marks =  [180, 200, 250, 130, 100, 300]
for m in marks:
    print(m)



l = len(marks)
i = 0

while i < l:
    print(i)
    i+= 1





marks =  [180, 200, 250, 130, 100, 300]
max = marks [0]
for m in marks:
    if m > max:
        max = m

print(max)

# list comprehension
# formula:[expression for item in iterable if condition]


numbers = [1, 2, 3, 4, 5, 6]
result = [i for i in numbers]

print(result)



numbers = [1, 2, 3, 4, 5, ]
result = [i*i for i in numbers]

print(result)



result = [i for i in range(1, 6)]
print(result)



numbers = [1, 2, 3, 4, 5, 6]
result = [i for i in numbers if i % 2 == 0]

print(result)



# list functions:
# 1 append
# 2 extend
# 3 insert
# 4 remove
# 5 pop
# 6 clear
# 7 sort
# 8 reverse
# 9 len



# append function example
numbers = [1,2,3]
numbers.append(4)
print(numbers)


# extend function example
a = [1,2]
b = [3,4]
a.extend(b)
print(a)


# insert function example
a = [1,3]
a.insert(1,2)
print(a)


# remove function example
a = [1, 2, 3, 4,]
a.remove(1)
print(a)


# pop function example
a = [1, 2, 3, 4]
a.pop()
print(a)


# clear function example
a = [1, 2, 3, 4]
a.clear()
print(a)


# sort function example
a = [4, 3, 2, 1]
a.sort()
print(a)


# reverse function example
a = [1, 2, 3, 4]
a.reverse()
print(a)


# length function example
a = [1, 2, 3, 4]
print(len(a))





# list comprehension example
numbers = [1, 2, 3, 4,5, 6, 7, 8, 9]

result = [i*2 for i in numbers if i % 2 == 0]
print(result)






# index example
# a = ["apple", "mango", "banana", "pine apple", "water milon", "grapes"]
# item             index
# apple              0
# mango              1
# banana             2
# pine apple         3
# water millon       4
# grapes             5







# pop function example
a = ["cat", "dog", "cow"]
a.pop(0)
print(a)




