string = str(input("string: "))
def compute_length(string):
    z = 0
    for i in string:
        z += 1
    return z
print("length of string: ",compute_length(string))

