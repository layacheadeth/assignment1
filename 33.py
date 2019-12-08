from math import *
class point:
    x=0
    y=0
    def translate(self,x,y):
        self.x+=x
        self.y+= y
    def distance_from_origin(self):
        return sqrt(self.x*self.x+self.y*self.y)
    def distance(self,other):
        dx=self.x-other.x
        dy=self.y-other.y
        return sqrt(dx*dx+dy*dy)
    def translate(self,dx,dy):
        
#main
p1=point()
p1.y=3
print(p1.x)


