class person:
    def init(self,name="deth",address="61A"):
        self.name=name
        self.address=address
    def getName(self):
        return self.name
    def setName(self,name):
        self.name=name
    def getAddress(self):
        return self.address
    def setAddress(self,address):
        self.address=address
class student(person):
    def _init_(self, numCourses=0, courses=[], grades=[]):
        super().init(name="deth",address="61A")
        self.courses = courses
        self.grades = grades
        self.numCourses = numCourses
    def addCourseGrade(self,course,grades):
        self.courses.append(course)
        self.grades.append(grades)
    def printGrades(self):
        for i in range(0,len(self.courses)):
            print("course :",self.courses[i], "\ngrade :", self.grades[i])

    def getAverageGrade(self):
        return sum(self.grades)/ len(self.grades)

    def _repr_(self):
        return "(%s, %s)" % (self.courses, self.grades)
class Teacher(person):
    pass
    def init(self,numCourses,courses):
        self.numCourses=numCourses
        self.courses=courses
    def addCourse(self,courses):
        courses=str(input("courses: "))
        for i in courses:
            if i == self.courses:
                return false
            return self.courses

people = person()
people.setName("beauty")
print(people.getName())
people.setAddress("4532")
print(people.getAddress())
students=student()
students.addCourseGrade("fashion",75)
students.printGrades()
teachers=teacher()
teachers.addCoursesGrade("fashion",89)
students.printGrades()
