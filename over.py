string=input("enter some integer value").split()
newlis=[]
for i in string:
    if int(i) > 100:
        newlis.append('over')
    else:
        newlis.append(i)
print(newlis)        
    
