# file handling
# file handling is the process of creationg, reading, writing, updating and closing files in a program

file = open("student.txt", "w")
file.write("My name is Owais")
file.close()

file = open("student.txt", "a")
file.write("\nMy Father name is Saif-ur-Rehman\nI am 16 years old\nI am live in Karachi\nI am learning Python")
file.close

file = open("student.txt", "r")
print(file.read())
file.close()



file = open("Test.file1", "w")
for i in range(10):
    file.write("My Father name is Saif-ur-Rehman\n")
file.close()



file = open("marks.txt", "w")
file.write("Urdu = 95\nMath = 79\nPhysics = 82\nChemistry = 88\nEnglish = 71")
file.close()



file = open("marks.txt", "a")
file.write("\nSindhi = 91\nComputer = 97")
file.close()



file = open("Test.file2", "w")
file.write("Math = 92\nComputer = 98")
file.close()


file = open("Test.file2", "a+")
file.write("\nEnglish = 81\nUrdu = 94")
file.seek(0)
print(file.read())
file.close()


file = open("skills_w_plus.text", "w+")
file.write("Python skills\n")
file.write("1. Variables\n")
file.write("2. Data Types\n")
file.write("3. Type Casting\n")
file.write("4. Input and Output\n")
file.write("5. Operators\n")
file.write("6. If statement\n")
file.write("7. If Else\n")
file.write("8. Nested If\n")  
file.write("9. Match Case\n")
file.write("10. For Loop\n")
file.write("11. While Loop\n")
file.write("12. Functions\n")
file.write("13. Modules\n")
file.write("14. Exception Handling\n")
file.write("15. File Handling\n")
file.write("16. OOP\n")
file.write("17. Numpy\n")
file.write("18. Pandas\n")

file.seek(0)
print(file.read())
file.close()


file = open("student.txt2", "w")
file.write("Name: Owais\nClass: 9\nAge: 16\nCity: Peshawar")
file.close()


file = open("student.txt2", "r+")

print(file.read())
file.write("\nSkill: Python")
file.seek(0)
print(file.read())
file.close()
