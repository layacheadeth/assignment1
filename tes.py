xlist2 = list(range(-3,6,2))
print(xlist2)
x=0
while x<10:
    print(x)
    x +=1
current_number = 0
while current_number < 10:
    current_number +=1
    if current_number % 2 == 0:
        continue
    print(current_number)
liz = ['ellis','ellis','damn','you']
while 'ellis' in liz:
    liz.remove('ellis')
print(liz)
x= float(input("x: "))
y= float(input("y: "))
def f3(x,y):
    print(x + y)
    return [x + y]
print("total: ",f3(x,y))
xlist = [3, 2, 1, 0]
for item in xlist:
    print(item, end=" ")