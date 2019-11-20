student1 = float(input("score of student1: "))
student2 = float(input("score of student2: "))
student3 = float(input("score of student3: "))
total = student1 + student2 + student3
def average(total):
    return ((total)/3.0)
print("average score of students:  ", average(total))
