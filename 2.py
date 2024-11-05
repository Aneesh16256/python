class Rectangle:
    def __init__(self,length,bredth):
        self.length=length
        self.bredth=bredth
    def perimeter(self):
        perimeter=2*self.length + 2*self.bredth
        return perimeter
    def area(self):
        area=self.length*self.bredth
        return area
    def equal(self,self2):
        if self.length==self2.length and self.bredth==self2.bredth:
            return True
    def not_equal(self,self2):
        if self.length!=self2.length and self.bredth==self2.bredth:
            return False
rectangle1 = Rectangle(4, 5)
rectangle2 = Rectangle(4, 5)
print(f"rectangle1 length= {rectangle1.length}")
print(f"rectangle1 breadth= {rectangle1.bredth}")
print(f"rectangle2 length= {rectangle2.length}")
print(f"rectangle2 breadth= {rectangle2.bredth}")
print(f"perimeter= {rectangle1.perimeter()}")
print(f"area= {rectangle1.area()}")
print(rectangle1.equal(rectangle2))
print(rectangle1.not_equal(rectangle2))