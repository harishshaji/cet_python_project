num = input("Enter a Number : ")
num = int(num)
new = 0
check = num
while num > 0:
    r = num % 10
    new = new + (r * r * r)
    num = int(num / 10)
if new == check:
    print(check,"is an armstrong number")
else:
    print(check,"is not an armstrong number")
