ids=[]
names=[]
ages=[]
n=int(input("n: "))
class fridge:
    def store():
        for i in range(n):
            id=int(input("id: "))
            name=str(input("name; "))
            age=int(input("age: "))
            ids.append(id)
            names.append(name)
            ages.append(age)
    def output():
            print("id: ",ids)
            print("name: ",names)
            print("age: ",ages)
    def update_age():
        nage=int(input("new_age: "))
        pos=int(input("adjusted_position: "))
        if pos>n:
            print("index out of range")
        else:
            for i in ages:
                if i == ages[pos]:
                    ages[pos]=nage
    def update_id():
        nid=int(input("new_id: "))
        pos=int(input("adjusted_id: "))
        if pos>n:
            print("index out of range")
        else:
            for i in ids:
                if i == ids[pos]:
                    ids[pos]=nid
    def update_name():
        nname=str(input("new_name: "))
        pos=int(input("adjusted_name: "))
        if pos>n:
            print("index out of range")
        else:
            for i in names:
                if (i,names[pos], i == names[pos]):
                    names[pos]=nname

fridge.store()
fridge.output()
fridge.update_id()
fridge.output()
fridge.update_name()
fridge.output()
fridge.update_age()
fridge.output()