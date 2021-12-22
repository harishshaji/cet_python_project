a = input("enter some number").split()
a = map(int,a)
b = [x for x in a if x>0]
print("positive no in list:", b)

