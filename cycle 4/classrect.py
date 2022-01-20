class rect:

    def __init__(self,length,breath):
        self.length = length
        self.breath = breath
        

    def area(self):
        area = self.length * self.breath
        return area

    def perimeter(self):
        peri = 2 * (self.length + self.breath)
        print("Perimeter of ur rectangle:",peri)    

    def compare(self,ob):
        a1 = self.area()
        a2 = ob.area()
        if a1 == a2 :
            print("Both rectangle have equal area")
        else :
            print("Both have different area")    



l= int(input("Enter length for your rectangle 1:")) 
b= int(input("Enter breath for your rectangle 1:"))        

ob1 = rect(l,b)
ob1.perimeter()
print("Area of ur rectangle is:",ob1.area())

l= int(input("Enter length for your rectangle 2:")) 
b= int(input("Enter breath for your rectangle 2:"))         

ob2 = rect(l,b)
ob2.perimeter()
print("Area of ur rectangle is:",ob2.area())

ob1.compare(ob2)

 




        