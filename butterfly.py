n = int(input('Enter rows'))
for i in range(n):
    for j in range(i,n):
        print(" ",end = " ")
    for k in range(i+1):
        print('*', end = " ")
    print()
for i in range(1,n):
    for j in range(i+1):
        print(" ",end = " ")
    for k in range(i,n):
        print('*', end = " ")
    print()