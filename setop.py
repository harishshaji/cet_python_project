lis1=input('enter some integer value for first list').split()
lis2=input('enter some integer value for second list').split()
lis1 = list(map(int, lis1))
lis2 = list(map(int, lis2))
n=len(lis1)
m=len(lis2)
if m==n:
    print('length of both list are equal')
else:
    print('length of both list are not equal')
    
r=sum(lis1) 
s=sum(lis2)        
if r==s:
    print('sum of lists are equal')
else:
    print('sum of lists are not equal')
if set(lis1) == set(lis2):
    
    print('both list have same elements')
else
    print('both list have different elements')
