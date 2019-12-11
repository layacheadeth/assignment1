import math
class Circle:
    def _init_(self,radius=1.0,color="red"):
        self.color = color
        self.radius = radius
    def getRadius(self):
        return self.radius
    def getColor(self):
        return self.color
    def setColor(self,color):
        self.color = color
    def setRadius(self,radius):
        self.radius = radius
    def __rep__(self):
        return {"radius":self.radius, "color": self.color}
    def getArea(self,radius):
        return math.pi * (self.radius**2)
circle1 = Circle()
print(circle1.__repr__())
print(circle1.getArea())

class Cylinder(Circle):
    def _init_(self, height=1.0):
        super()._init_(radius=1.0,color="red")
        self.height = height
    def getHeight(self):
        return self.height
    def setHeight(self,height):
        self.height = height
    def _repr_(self):
        return {"radius":self.radius, "color": self.color, "height": self.height}
    def getVolume(self):
        return self.getArea() * self.height
cylinder1 = Cylinder()
print(cylinder1._repr_())
print(cylinder1.getVolume())