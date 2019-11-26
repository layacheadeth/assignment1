x = float(input("x: "))
y = float(input("y: "))
def condition(x,y):
    if x > y:
        return x
    elif x < y:
        return y
print("max is: ",condition(x,y))