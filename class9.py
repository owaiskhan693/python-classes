# sets type practice
# "A set is an unordered collections of unique items duplicate values are not allowed".

fruits = {"apple", "banana", "mango"}

print(fruits)
print(type(fruits))


numbers = {10, 20, 30, 40, 10, 20}

print(numbers)


animals = {"cat", "dog", "cow", "goat"}

print(len(animals))


fruits = {"apple", "mango", "orange", "grapes"}

print("grapes" in fruits)
print("mango" in fruits)



colors = {"white", "black", "green", "red", "blue", "purple",}
print(colors)
print(len(colors))


# for loop and while loop used in sets
fruits ={"apple", "mango", "orange", "grapes", "water milon"}

for fruits in fruits:
    print(fruits)


numbers = {10, 20, 30, 40, 50} 

for num in numbers:
    print(num)


numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9,} 

for num in numbers:
    if num % 2 == 0:
        print(num)



fruits ={"apple", "mango", "orange", "grapes", "water milon"}

fruit_list = list(fruits)

i = 0

while i < len(fruit_list):
    print(fruit_list[i])
    i+= 1


names = {"owais", "junaid", "obaid", "ahmed", "shakeel"}   

name_list = list(names)

i = 0

while i < len(name_list):
    print(name_list[i])
    i+= 1



letters = {"a", "b", "c", "d", "e", "f", "g", "h", "i"}

for x in letters:
    if x in "aeiou":
        print(x)



numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

for num in numbers:
    if num == 5:
        continue
    print(num)



numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

for num in numbers:
    if num == 8:
        break
    print(num)



animals = {"cat", "dog", "cow", "goat"}

a = list(animals)

i = 0

while i < len(a):
    print(a[i])
    i += 1


skills = {"Python", "HTML", "CSS", "Python"}   

print(skills)


skills = {"Python", "HTML", "CSS", "Python"}

for skills in skills:
    print(skills)



languages = {"Pashto", "Balochi", "Urdu",}

if "Pashto" in languages:
    print("Person Pashto janta hain")


languages = {"Pashto", "Balochi", "Urdu",}

lang_list = list(languages)

i = 0

while i < len(lang_list):
    print(lang_list[i])
    i += 1



Person1 = {"Python", "HTML", "CSS",}
Person2 = {"Python", "Java", "HTML"}

print(Person1 & Person2)



hobbies = {"Cricket", "Football", "Cricket", "Reading"}

print(hobbies)



hobbies = {"Cricket", "Football", "Reading"}

for hobby in hobbies:
       print(hobby)



Person = {"Owais", 16, "Karachi"}

print(Person)



Person = {"Owais", 16, "Karachi"}

for info in Person:
    print(info)



Person = {"Owais", 16, "Karachi"}

data = list(Person)

i = 0

while i < len(data):
    print(data[i])
    i += 1


# slicing practice
Person = {"Owais", 16, "Karachi", "Cricket", "Python"}

data = list(Person)

print(data[0:3])



# set functions:
# 1 add
# 2 remove
# 3 discard
# 4 pop
# 5 update


fruits = {"apple", "mango", "orange"}

fruits.add("banana")
print(fruits)


fruits = {"apple", "mango", "orange"}

fruits.remove("mango")
print(fruits)


fruits = {"apple", "mango", "orange"}

fruits.discard("orange")
print(fruits)


fruits = {"apple", "mango", "orange", "water milon", "grapes"}

item = fruits.pop()

print(item)
print(fruits)


set1 = {"apple", "banana", "mango"}
set2 = {"orange", "water milon", "grapes"}

set1.update(set2)

print(set1)



# sets functions name:
# 1 add
# 2 remove
# 3 discard
# 4 pop
# 5 update
# 6 clear
# 7 union
# 8 intersection
# 9 difference
# 10 symmetric_difference
# 11 is.subset
# 12 is.superset
# 13 is.disjoint


# add
# Adds a single element to a set
fruits = {"apple", "banana", "mango"}
fruits.add("orange")
print(fruits)

# remove
# Removes a specified element from a set (gives error if not found)
fruits = {"apple", "banana", "mango"}
fruits.remove("mango")
print(fruits)

# update
# Adds multiple element to a set
A = {1,2,3}
A.update([4, 5, 6])
print(A)


# discard
# removes an element if it exists (no error if not found)
A = {1, 2, 3,}
A.discard(3)
print(A)


# pop
# removes and returns a random element from a set
A = {1, 2, 3}
A.pop()
print(A)

# clear
# removes all elements from a set
A = {1, 2, 3}
A.clear()
print(A)


# union
# returns all elements from both sets
A = {1, 2, 3}
B = {4, 3, 6}
print(A.union(B))


# intersection
# returns only common elements of two sets
A = {1, 2, 3}
B = {3, 5, 1}
print(A.intersection(B))


# difference
# returns elements that are in first set but not in second set
A = {1, 2, 3}
B = {2, 3}
print(A.difference(B))


# difference update
# removes all elements pf another set from the original set and updates it
A = {"apple", "banana", "mango"}
B = {"mango", "water milon", "apple"}
A.difference_update(B)
print(A)



# symmetric_difference
# returns elements that are not common in both sets
A = {1, 2, 3, 4}
B = {5, 1, 4, 8}
print(A.symmetric_difference(B))



# issubset
# checks if all elements of one set are present in another set
A = {1, 2,}
B = {3, 4}
print(A.issubset(B))



# issuperset
# checks if a set contains all elements of another set
A = {1, 2, 3, 4}
B = {1, 2,}
print(A.issuperset(B))


# isdisjoint
# check if two sets have no common elements
A = {1, 2, 3, 4}
B = {5, 6, 7}
print(A.isdisjoint(B))


# copy
# returns a copy of a set
A = {1, 2, 3, 4}
B = A.copy()
print(B)
