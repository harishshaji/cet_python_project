def factors(num):
    factorlis = []
    for i in range(1,num+1):
        if (num % i) == 0:
            factorlis.append(i)
    print("factorial of ",num,"is",factorlis) 

num = int(input("enter your number"))

factors(num)