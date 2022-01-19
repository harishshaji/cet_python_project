from graphics import *

def rect():

    l = int(input("Length of rectangle"))
    b = int(input("Breath of rectangle"))
    rectarea,rectperimeter = rectangle(l, b)
    print("Area of rectangle =",rectarea)
    print("Peremeter of rectangle =",rectperimeter)

def cir():

    r = int(input("Radius of circle"))
    circlearea,circleperemeter = circle(r)
    print("Area of circle =",circlearea)
    print("Peremeter of circle =",circleperemeter)

def cub():    

    le = int(input("Length of cuboid"))
    br = int(input("Breath of cuboid"))
    he = int(input("Height of cuboid"))
    cuboidarea,cuboidperemeter = cuboid(le,br,he)
    print("Area of cuboid =",cuboidarea)
    print("Peremeter of sphere =",cuboidperemeter)

def sph():    

    sr = int(input("Radius of sphere"))
    spherearea,sphereperimeter = sphere(sr)
    print("Area of sphere =",spherearea)
    print("Peremeter of sphere =",sphereperimeter)


while(1):
    
    print("\n_________________MENU_________________\n")
    print("Enter a option from following:")    
    ch = int(input("1.Rectangle\n2.Cicle\n3.Cuboid\n4.Sphere\n5.Exit"))
    if ch == 1:
        rect()
    elif ch == 2:
        cir()
    elif ch == 3:
        cub()
    elif ch == 4:
        sph()
    elif ch == 5:
        print("Program terminated...")
        exit()
    else:
        print("Enter a valid option")    
                        
    
