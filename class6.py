# continue and break mix practice:
i = 1
while i <= 10:
    if i == 6:
       break
    print(i)
    i += 1


i = 0

while i < 10:
    i += 1
    if i == 4:
        continue
    print(i)




i = 0

while i < 15:
    i += 1
    if i % 2 == 0:
        continue
    print(i)




i = 1

while i <= 10:
    result = 2 * i

    if result > 20:
        break

    print("2 x ", i, "=", result)
    i += 1




for i in range(1, 21):
    if i == 3 or i == 7:
        continue
    print(i)



for i in range(1, 16):
    if i % 2 == 0:
        continue
    print(i)
    

for i in range(1 , 11):
    if i == 5:
        continue
    print(i)




for i in range(1, 11):
    if i == 7:
        break
    print(i)





name = "PYTHON"

for i in name:
    if i == "T":
        break
    print(i)
    

for i in range(1,20):
    if i == 10:
        break
    print(i)





for i in range(1,20):
    if i == 15:
        continue
    print(i)



word = "PYTHON"

for ch in word:
    if ch == "O":
        continue
    print(ch)


