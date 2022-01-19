from math import *
print("Subpackage dgraphics is imported")

def cuboid(l,b,h):
    
    cuboidarea = 2 * (l * b + b * h + l * h)
    cuboidperemeter = 4 * (l + b + h)
    return cuboidarea,cuboidperemeter

def sphere(r):
    
    spherearea =  4 / 3 * r * r *r * pi
    spherperemeter = 4 * pi * r * r
    return spherearea,spherperemeter