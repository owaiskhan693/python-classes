# Exception Handling
# Exception handling Python ka wo tareeqa hain jis se program chalne ke dauran aane wali errors (exceptions) ko handle kiya jata hain taake program achanak band na ho.

# print("start")
# a = 10
# b = 20
# if b < 10:
#     z = a / b
# else:
#    z = a + b + c
# print(z)
# print("End")




# print("start")
# a = 10
# b = 20
# try:
#     if b < 10:
#      print("If")
#      z = a / b
#     else:
#        print("Else")
#        z = a + b 
#     print(z)
# except:
#    print("Except")


# print("End")

print("Program start")
x = 10
y = 20
try:
   if y < 10:
      print("If")
      z = x / y
   else:
      print("Else")
      z = x + y 
   print(z)
except ZeroDivisionError as e:
   print("ZeroDivisionError=", e)
except NameError as e:
   print("in NameError=", e)
except Exception as e:
   print("in Exception=", e)
else:
   print("Else of try")
finally:
   print("In finally block")

print("End")


print("Program Start")


try:
   file = open("student.text", "r")
   print(file.read())
   file.close

except FileNotFoundError :
   print("FileNotFoundError: File not found.")

else:
   print("File Opened Sucessfully")
finally:
   print("Program End")





print("Program Start")


try:
   x = "10"
   y = 5
   print(x + y)

except TypeError :
   print("TypeError: cannot add string and integer.")

else:
   print("No error occured")
finally:
   print("Program End")



print("Program Start")


try:
   x = int(input("Enter a Number:"))
   print("Number =", x)

except ValueError :
   print("ValueError: Please enter a valid integer.")

else:
   print("No error occured")
finally:
   print("Program End")




print("Program Open")

try:
   x = int(input("Enter a First Number:"))
   y = int(input("Enter a Second Number"))
   
   result = x / y
   print("Result=", result)

except:
   print("I you Except")
else:
   print("Block Else")
finally:
   print("Program Close")

   

