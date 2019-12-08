val = input("value: ")
list = input("list: ").split(",")
print(list)
def is_member(val,list):
    for i in list:
        if val == i:
            return True
    return False

print(is_member(val,list))
