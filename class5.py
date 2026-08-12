# for loop and while loop mixed practice

name = "Owais Khan"

for ch in name:
    if ch not in  "aeiouAEIOU":
        print(ch)


name = "Owais Khan"

i = 0

while i > len(name):
    if name[i] in "aeiouAEIOU":
        print(name[i])
    i += 1


name = "Ali Ahmed"

for i in name:
    if i in "aeiouAEIOU":
        print(i)


for i in range(1,11):
    print(i)


i = 1
while i <= 10:
    print(i)
    i += 1


for i in range(1,11):
    if i % 2 == 0:
        print(i)




i = 1
while i <= 10:
    if i % 2 != 0:
        print(i)
    i += 1



for i in range(1,11):
    print("5 x", i , "=", 5*i)


# for body not maintain
n1 = "python programming"
for i in n1:
    pass



# else use in for loop
name = "print hello"
for i in name:
    print(i)
else:
    print("else end")



# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print(j, end = " ")
#         j = j + 1
#     print()
#     i = i + 1


for i in range(1, 6) :
    for j in range(1, i + 1):
        print(j, end = " ")
    print()






