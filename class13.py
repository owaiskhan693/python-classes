# Find a Prime Number
def check_number(x):
    is_prime = True
    i = 2

    while i < x:
      if x % i == 0:
        is_prime = False
        break
    i = i + 1
    return is_prime



x = int(input("Please enter any Number"))
flag = check_number(10)
if flag :
        print("Number is a Prime")
else:
         print("Number is not a prime")


    

