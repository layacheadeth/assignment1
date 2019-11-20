class1=32
class2=45
class3=51
def studentclass1(class1):
    return (class1/5)
def leftover1(class1):
    return (class1%5)
def studentclass2(class2):
    return (class2%7)
def leftover2(class2):
    return (class2%7)
def studentclass3(class3):
    return (class3/6)
def leftover3(class3):
    return (class3%6)
print("class1: \t"+ "leftover: ",studentclass1(class1),leftover1(class1))
print("class2: \t" +"leftover: ",studentclass2(class2),leftover2(class2))
print("class1: \t" +"leftover: ",studentclass3(class3),leftover3(class3))