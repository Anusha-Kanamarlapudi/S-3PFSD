from abc import ABC
class Calculate(ABC):
    def Perimeter(self):
        pass
    def area(self):
        pass

class Rectangle(Calculate):
        def Perimeter(self,c,d):
            self.c=c
            self.d=d
        perimeter=2*(c*d)
        print("Perimeter is"+perimeter)
        def  area(self,a,b):
            self.a=a
            self.b=b
            area=a*b
            print("Area is"+area)

re=Rectangle()
re.Perimeter(10,20)
re.area(10,20)


