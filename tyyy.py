def foo():
    xlist = []
    for i in range(4):
        x = input("Enter a number: ")
        xlist.append(x)
    return xlist
print(foo())
#
xlist= [2,3,1]
ylist=xlist.sort()
print(xlist,ylist)
#
def get_formatted_name(first_name,last_name,middle_name = ""):
    if middle_name != "":
        name = first_name + " " + last_name
    else:
        name = first_name + " " +middle_name+ last_name
    return name
print(get_formatted_name('john','lee','hookie'))
