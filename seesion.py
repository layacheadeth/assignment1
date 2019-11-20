space = ' '
star = '*'
amount = 5
for i in range(0,4):
    print((space * (amount - i ) + star * (i + 1)))
for i in range(0,5):
    print((space * (i + 1)) + star * (amount - (i)))

