# vowels print

text = "hello world"
vowels = "aeiou"

i = 0

while i < len(text):
    if text[i] in vowels:
        print(text[i])
    i += 1





# vowels not in
text = "hello world"
vowels = "aeiou"

i = 0

while i < len(text):
    if text[i] not in vowels:
        print(text[i])
    i += 1





# for loop practice

for x in range(3):
    print(x,"python")




for y in range(50):
    print(y, "hello word")


numbers = [1, 2, 3]

for n in numbers:
    print(n)
    print("programming")


numbers = [50, 60, 90]

for n in numbers:
    print(n + 10)


names = ("junaid", "ahmed", "sarfaraz")

for x in names:
    print(x)



marks = (10, 20, 30)

for m in marks:
    print(m)





marks = (10, 20, 30)

for m in marks:
    print(m + 40)





numbers = [4, 8, 12]

for n in numbers:
    print(n * 2)




for i in range(3):
    for j in range(2):
        print(i , j)
    