# Python Stack Implementation
# Queue First Come First Serve
# Stack First Come Last Serve


# Stack
# Stack ek data structure hai jisme data is tarah store hota hain ke jo item sab se akhir mein add hota hain wahi sab se pehle nikalta hai

stack = []

while True:
    x = input("Enter 1 to push \n Enter 2 to pop \n Enter 0 to exit")
    if x == '0':
        break
    elif x == '1':
        name = input("Enter item to push :")
        stack.append(name)
    elif x == '2':
      if len(stack) <= 0:
          print("Stack is empty, you can not pop any item")
      else:
          x = stack.pop()
          print(f"Pop item is {x}")
    else:
        print("Invalid Input")
        print(stack)



stack = []

while True:
    print("\n. Push")
    print("\n. Pop")
    print("\n. Show")
    print("\n. Exist")
    choice = int(input("Enter your choice:"))
    if choice == 1:
      item = input(("Enter item:"))
      stack.append(item)
    elif choice == 2:
     if len(stack) <= 0:
        print("Stack is Empty")
     else:
        print("Removed:", stack.pop())

    elif choice == 3:
      print("Stack:", stack)

    elif choice == 4:
      print("Program End")
      break

else:
    print("Invalid Choice")


        


# Queue
# Queue ek linear data structure hai jo FIFO (First In, First Out) ke rule par kam karti hai. Matlab jo element sab se pehle add hota hai, woh sab se pehle remove hota hai.
from collections import deque

queue = deque()

while True:
   print("\n1. Enqueue")
   print("\n2. Dequeue")
   print("\n3. Show")
   print("\n4. Exit")

   choice = int(input("Enter your Choice:"))
   if choice == 1:
      item = input("Enter item:")
      queue.append(item)
      print(item, "added to queue")

   elif choice == 2:
      if len(queue) <= 0:
         print("Queue is Empty")
      else:
        item = queue.pop(0)
        print(item, "removed from queue")

   elif choice == 3:
      if len(queue) <= 0:
         print("Queue is Empty")
      else:
         print("Queue elemets are:", queue)

   elif choice == 4:
      print("Program End")
      break
   
else:
   print("Invalid Input")




# Python code to demonstrate Implementing 
# stack using list
stack = ["Amar", "Akbar", "Anthony"]
stack.append("Ram")
stack.append("Iqbal")
print(stack)

# Removes the last item
print(stack.pop())

print(stack)





# Python code to demonstrate Implementing 
# Queue using list
queue = ["Amar", "Akbar", "Anthony"]
queue.append("Ram")
queue.append("Iqbal")
print(queue)

# Removes the first item
print(queue.pop(0))

print(queue)

# Removes the first item
print(queue.pop(0))

print(queue)




   