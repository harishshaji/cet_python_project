def fact(num):
   
    if num == 1 or num == 0:
        return 1
    f=num*fact(num-1)
    return f
    
num = int(input("enter a number"))
k=fact(num)
print("factorial",num,"is", k)            
