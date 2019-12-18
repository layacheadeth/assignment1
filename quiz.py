ids=[]
names=[]
positions=[]
salarys=[]
var idss:str
var i:int
var j:int
var namess:str
var positionss:str
var salaryss:int
def newstaff():
    idss = input("id: ")
    if len(idss) > 5 and len(idss) < 5:
        print('the length must be 5 charactor')
    for i in idss:
        if i != 's':
            print('the first charactor must be letter S')
    j: int
    for i in idss(1, 5):
        if i != j
            print('all of the letter from here must be numeric')
    # b
    namess = input('name: ')
    if len(namess) > 20:
        print('name should not be more than 20 charactors')
    # c
    positionss = input('position: ')
    if positionss != 'Staff' or positionss != 'Officer' or positionss != 'Manager':
        print('input again(the input must be either(Officer,Manager,Staff)')
    # d
    salaryss = int(input("salary: "))
    if positionss == 'Staff':
        if salaryss < 3500000 and salaryss > 70000000:
            print('input again salary should be 3500000<salary<70000000')
        else:
            print('input correct')
    if positionss == 'Officer':
        if salaryss < 7000001 and salaryss > 10000000:
            print('input again salary should be 7000001<salary<10000000')
        else:
            print('input correct')
    if positionss == 'Manager':
        if salaryss < 10000000:
            print('input again salary should be salary>10000000')
        else:
            print('input correct')
def deletestaff():
    staff_id = input("staff_id:")
    for i in ids:
        if staff_id in ids:
            print('it is in')
            ids[i].remove()
        else:
            print('it is not')
def view_summary_data():
    print('1.Staff\n')
    print('Maximum Salary: 4500000\n')
    print('Minimum Salary: 7000000\n')
    print('Average Salary: 4750000\n')
    print('2.Officer\n')
    print('Maximum Salary: 8500000\n')
    print('Minimum Salary: 8500000\n')
    print('Average Salary: 8500000\n')
    print('3.Officer\n')
    print('Maximum Salary: 10700000\n')
    print('Minimum Salary: 10700000\n')
    print('Average Salary: 10700000\n')
n=int(input("n: "))
file=open("data.txt","w")
file.write()
for i in range(n):
    id=(input("id: "))
    name=input("name: ")
    position=input("position")
    salary=int(input("salary: "))
    ids.append(id)
    names.append(name)
    positions.append(position)
    salarys.append(salary)
for j in range(n):
    print('id: ',ids[j])
    print('name: ', names[j])
    print('position: ', positions[j])
    print('salary: ', salarys[j])
file.close()
file=open('data.txt','r')
#c
print('1.Newstaff')
print('2.Delete staff')
print('3.View Summary Data')
print('4.Save and Exit')
ch=int(input("choose 1[1-4]:"))
#D
switch (ch):
    case 1:
        newstaff()
#e
    case 2:
        deletestaff()
    case 3:
        view_summary_data()
    case 4:
        with open('data.txt','w') as f:


    default:print('error inputting')
