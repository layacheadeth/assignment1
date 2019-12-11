class circle:
    def __init__(self,radius=1.0,color="red"):
        self.radius=radius
        self.color=color
    def getRadius(self):
        return self.radius
    def setRadius(self,radius):
        radius=float(input("radius: "))
        self.radius = radius
    def getColor(self):
        return self.color
    def setColor(self,color):
        self.color=str(input("color:"))
    def toString(self):
        return{"radius":self.radius,"color":self.color}
    def getArea(self,radius):
        return (3.14*3.14)*self.radius
class cylinder(circle):
    pass
    def __init__(self,height=1.0):
        self.height=height
    def getHeight(self):
        a=self.height
        return a
    def setHeight(self,height):
        self.height=float(input("height: "))
    def toString(self):
        return {"height":self.height}
    def getVolume(self,height,radius):
        v=((3.14)*(radius*radius)*self.height)/3
        return v
#
deth=circle()
deth.setRadius(23)
print(deth.getRadius())
deth.setColor("red")
print(deth.getColor())
print(deth.getArea(2))
print(deth.toString())

lay=cylinder(circle)
lay.setHeight(23)
print(lay.getHeight())
print(lay.getVolume(3,3))
print(lay.toString())
