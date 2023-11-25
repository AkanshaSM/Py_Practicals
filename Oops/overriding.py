class Shape:
    def area(self):
        return 0
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return f"the area of circle is {3.14*self.radius*self.radius}"
class Rectangle(Shape):
    def __init__(self,length,width):
         self.length=length
         self.width=width
    def area(self):
        return f"the area of a rectangle is {self.length*self.width}"
c=Circle(2)
r=Rectangle(3,5)
print(c.area())
print(r.area())

         
    
    
 
    
    
    