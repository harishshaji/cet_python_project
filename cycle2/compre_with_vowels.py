a = input("enter a word")
a = a.lower()
l = ['a','e','i','o','u']
b = [x for x in a if x in l]
print(b) 

