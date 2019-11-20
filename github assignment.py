list = ["deth","lay","ace"]
for i in range(0,3):
    print(list[i] +" "+ "you are invited")
print(list[2]+" "+"couldn't come")
del list[2]
list.insert(2,"luffy")
for i in range(0,3):
    print(list[i]+ " "+ "you are invited")
print("we have found a bigger table for the party")
list.insert(0,"nami")
list.insert(2,"sanji")
list.append("zoro")
for i in list:
    print(i +" " +"you are invited")
print("only two places are available for the dinner tonight")
while len(list) > 2:
        print(list.pop()+" "+"sorry we couldn't invite you to the party")
print(list)
del list[0:2]
print(list)

