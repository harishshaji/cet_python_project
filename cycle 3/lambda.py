class shape:

    def rectangle(self):
        l = int(input("enter length of rectangle"))
        b = int(input("enter breath of rectangle"))
        a = lambda l,b:l*b
        area = a(l,b)
        print("area of rectangle is",area)

    def circle(self):
        r = int(input("enter radius of circle"))
        a = lambda r:3.14*r*r
        area = a(r)
        print("area of circle is",area)

    def triangle(self):
        h= int(input("enter height of triangle"))
        b = int(input("enter breath of triangle"))
        a = lambda b,h:b*h*0.5
        area = a(b,h)
        print("area of triangle is",area)

ob = shape()
ob.circle()
ob.rectangle()
ob.triangle()




