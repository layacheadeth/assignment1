class person:
    def __init__(self,name="deth",address="61A"):
        self.name=name
        self.address=address
    def getName(self):
        return self.name
    def setName(self,name):
        self.name=str(input("name: "))
    def getAddress(self):
        return self.address
    def setAddress(self,address):
        self.address=str(input("address: "))
stu={}
class student(person):
    pass
    def __init__(self,numCourses=0,courses={},grades={}):
        self.numCourses=numCourses
        self.courses=courses
        self.grades=grades
    def addCourseGrade(self,courses,grades,n):
        self.n=int(input("n: "))
        for i in range(n):
            self.courses=input("Courses: ")
            self.grades=input("Grades: ")
            stu[courses] = grades
        for i in range(n):
            print(stu)
class Teacher(person):
    pass
    def __init__(self,numCourses,courses):
        self.numCourses=numCourses
        self.courses=courses
    def addCourse(self,courses):
        courses=str(input("courses: "))
        for i in courses:
            if i == self.courses:
                return false
            return self.courses

people = person()
people.setName("deth")
print(people.getName())
people.setAddress("61A")
print(people.getAddress())
students=student()
students.addCourseGrade("math","A",2)