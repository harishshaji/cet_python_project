a,c=input('enter 2 integer no').split()
a=int(a)
c=int(c)
if a > c:
    small = c
else:
    small = a
for i in range(1,small+1):
    if a%i == 0 and c%i == 0:
        gcd=i
print(i,'is the GCD')        
    
