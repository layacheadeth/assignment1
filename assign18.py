string = str(input("string: "))
def reverse(string):
    str= ""
    for i in string:
        str= i + str
    return str
print("reverse string: ",reverse(string))
# first it get letter d then it get letter e to put infront since it's i+ str not str + i