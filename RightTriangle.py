rows = int(input('Enter number of rows'))

#Increasing Pattern:
for i in range(rows):
    for j in range(i+1):
        print('*',end = " ")
    print()

print()

#Decreasing Pattern:
for i in range(rows):
    for j in range(i,rows):
        print('*',end = " ")
    print()


for i in range(rows):
    for j in range(i,rows):
        print(' ',end = " ")
    for k in range(i+1):
        print('*',end = " ")
    for m in range(i):
        print('*',end = " ")
    print()
for i in range(rows):
    for j in range(i+1):
        print(' ',end = " ")
    for k in range(i,rows):
        print('*',end = " ")
    for m in range(i,rows-1):
        print('*',end = " ")
    print()
