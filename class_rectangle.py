class Rectangle:
    def __init__(self,length,bredth):
        self.length=length
        self.bredth=bredth
    def perimeter(self):
        perimeter=2*self.length + 2*self.bredth
        return perimeter
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side,side)

p1 = Rectangle(15, 6)
print(p1.length)
print(p1.bredth)
print("perimeter= ",p1.perimeter())

p2 = Square(4)
print(p2.perimeter())