x= float(input("x: "))
y= float(input("y: "))
z= float(input("z: "))
def max_of_three(x,y,z):
    if x > y:
        if x > z:
            max = x
    if y > x:
        if y > z:
            max = y
    if z > x:
        if z > y:
            max = z
    return max
print("max is:   ",max_of_three(x,y,z))
