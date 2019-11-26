list1 = str(input("list1: "))
list1s = list1.split()
list2 = str(input("list2: "))
list2s= list2.split()
def overlapping(list1s,list2s):
    for i in range(len(list1s)):
        for j in range(len(list2s)):
            if list1s[i] == list2s[j]:
                b ="true"
            else:
                b = "false"
            return b
print(list1s)
print(list2s)
print(overlapping(list1s,list2s))
