# A nested loop is a loop inside another loop. The outer loop runs once,and for each run of the other loop, the inner loop runs completely.
for row in range(1, 10):
    for col in range(1, 10):
        print("*", end=" ")
        print( ) # line change


for i in range(1, 5):
    for j in range(1, i+1):
        print(j, end=" ")
        print()



