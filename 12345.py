m = int(input("Enter Number Of RowA:"))
n = int(input("Enter The Number Of ColumnA:"))
Mata = []
for i in range (0,m):
    Mata.append([])
for i in range (0,m):
    for j in range (0,n):
        Mata[i].append(j)
        Mata[i][j]=0
for i in range (0,m):
    for j in range (0,n):
        print ('entry in row: ',i+1,'column: ',j+1)
        Mata[i][j] = int(input())
print(Mata)
m = int(input("Enter Number Of RowB:"))
n = int(input("Enter The Number Of ColumnB:"))
Matb = []
for i in range (0,m):
    Matb.append([])
for i in range (0,m):
    for j in range (0,n):
        Matb[i].append(j)
        Matb[i][j]=0
for i in range (0,m):
    for j in range (0,n):
        print ('entry in row: ',i+1,'column: ',j+1)
        Matb[i][j] = int(input())
print(Matb)
result = []
for i in range (0,m):
    result.append([])
for i in range (0,m):
    for j in range (0,n):
        result[i].append(j)
        result[i][j]=0
for i in range (0,m):
    for j in range (0,n):
        result[i][j] = Mata[i][j] + Matb[i][j]
print('answer of this 2 array:')
for r in result:
    print(r)

