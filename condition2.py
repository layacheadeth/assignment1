a = 8
def func1():
    adding = a*a
    multi = adding * 2
    mod = multi * 2
    return adding,multi,mod
x,y,z = func1()
print("adding: ",x)
print("multi:   ",y)
print("mod:    ",z)
