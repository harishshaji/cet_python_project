la = input("enter a list of color")
lb = input("enter second list of color")
la = la.split()
lb = lb.split()
la = set(la)
lb = set(lb)
lc = la.difference(lb)
print(lc)