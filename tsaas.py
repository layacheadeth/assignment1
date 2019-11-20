n=int(input("input n: "))
ids=[]
names=[]
tels=[]
maths=[]
cprograms=[]
physics=[]
totals=[]
averages=[]
grades=[]
for i in range(0,n):
    id=int(input("id: "))
    name=input("name: ")
    tel=input("tel: ")
    math=int(input("math: "))
    cprogram=int(input("cprogram: "))
    physic=int(input("physic: "))
    total=int(math+cprogram+physic)
    average=int((math+cprogram+physic)/3.0)
    ids.append(id)
    names.append(name)
    tels.append(tel)
    maths.append(math)
    cprograms.append(cprogram)
    physics.append(physic)
    totals.append(total)
    averages.append(average)
    if averages[i]<50:
        grade='F'
    elif averages[i]<60:
        averages='E'
    elif averages[i]<70:
        grade='D'
    elif averages[i]<80:
        grade='C'
    elif averages[i]<90:
        grade='D'
    elif averages[i]<100:
        grade='A'
    else:
        print('error inputting')
    grades.append(grade)
for j in range(0,n):
    print('id: ',ids[j])
    print('name: '+names[j])
    print('tel: '+tels[j])
    print('math: ',maths[j])
    print('cprogram:',cprograms[j])
    print('physic: ',physics[j])
    print('total: ',totals[j])
    print('average: ',averages[j])
    print('grade: ',grades[j])