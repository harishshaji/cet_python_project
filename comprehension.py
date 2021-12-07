a=input("enter a list")
a=a.split()
a=map(int,a)
b=[x for x in a if (x%2)!=0]
print(b)