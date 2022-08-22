class Rectangle:
    def perimeterofRectangle(self,a,b):
        return 2*(a+b)
    def areaofRectangle(self,a,b):
        return a*b
class Circle:
    def perimeterofCircle(self,r):
        return 2*3.14*r
    def areaofCircle(self,r):
        return 3.14*r*r
class Triangle:
    def perimeterofTriangle(self,s1,s2,s3):
        return s1+s2+s3;
    def areaofTriangle(self,s1,s2,s3):
        s=(s1+s2+s3)/2
        area=(s*(s-s1)*(s-s2)*(s-s3)) ** 0.5
        return area

ob1=Rectangle()
ob2=Circle()
ob3=Triangle()
print("Enter length and breadth of rectangle ")
print("AREA IS:",ob1.areaofRectangle(int(input()),int(input())))
print("PERIMETER IS:",ob1.perimeterofRectangle(int(input()),int(input())))
print("Enter radius of circle")
print("PERIMETER IS:",ob2.perimeterofCircle(int(input())))

print("AREA IS:",ob2.areaofCircle(int(input())))
print("Enter radius of TRIANGLE")
print("PERIMETER IS:",ob3.perimeterofTriangle(int(input()),int(input()),int(input())))

print("AREA IS:",ob3.areaofTriangle(int(input()),int(input()),int(input())))


