from dgraphics import *
from math import *

print("Graphics package is imported")

def rectangle(l,b):
    rectarea = l * b
    rectperemeter = 2 * (l + b)
    return rectarea,rectperemeter

def circle(r):
    circlearea = pi * r * r
    circleperemeter = 2 * pi * r 
    return circlearea,circleperemeter



