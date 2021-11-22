x = input("enter a string")
 
w = ""
for i in x:
    w = i + w
 
if (x == w):
    print(w,"is a palidrome string")
else:
    print(w,"is not a palidrome string")

