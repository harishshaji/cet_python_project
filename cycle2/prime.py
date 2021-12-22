a = int(input("enter a number"))
flag = 0;
n = a.len()
for i in range(0,n)
	if a % i == 0
		flag = 1
if flag == 0:
    print(a,"is Prime")
else:
    print(a,"is not Prime")
