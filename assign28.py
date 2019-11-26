val = str(input("value: "))
list = str(input("list: "))
lists = list.split()
def is_member(val,lists):
    for i in range(len(lists)):
        if val == lists[i]:
            a = "true"
        else:
            a = "false"
        return a
print(is_member(val,lists))
