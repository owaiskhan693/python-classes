# Tuple type practice
# "A tuple is an ordered and immutable collection of items in python".

names = ('ahmed', 'junaid', 'obaid')
print(names)
print(type(names))

names = ('ahmed', 'junaid', 'obaid')
print(names[0])
print(names[1])


names = ('ahmed', 'junaid', 'obaid')
print(len(names))

# for loop and while loop used in tuple practice 
names = ('ahmed', 'junaid', 'obaid')

for i in names:
    print(i)

animal_names = ('cat', 'dog', 'cow')

for i in animal_names:
    print(i)



names = ('ahmed', 'junaid', 'obaid')
i = 0

while i < len(names):
    print(names[i])
    i += 1



numbers = (10, 20, 30,)
i = 0

while i < len(numbers):
    print(numbers[i])
    i += 1

# tuple slicing practice
numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])


numbers = (10, 20, 30, 40)
print(numbers[0:3])



numbers = (10, 20, 30, 40)
print(numbers[2:])



numbers = (10, 20, 30, 40)
print(numbers[:3])



numbers = (10, 20, 30, 40)
print(numbers[0:])


# Tuple functions names:
# 1 count
# 2 index

# count and index mixex practice
numbers = (1, 2, 3, 4, 5, 6, 3, 8, 3, 3,)
print(numbers.count(3))



numbers = (1, 2, 3, 4, 5, 6, 3, 8, 3, 3,)
print(numbers.index(8))

fruits_names = ("apple", "banana", "orange")
print(fruits_names.index("banana"))


colors = ("white", "black", "red", "blue")
print(colors.index("white"))



numbers = (9, 2, 6, 4, 6, 6, 7, 6, 6, 10)
print(numbers.count(6))



# mixed practice

names = ("ahmed", "junaid", "obaid", "owais")
print(names[1:3])

for i in names:
    print(i)


print(names.count("owais"))

print(names.index("obaid"))

