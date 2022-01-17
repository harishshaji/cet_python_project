def length(lis):
    max = lis[0]
    size = len(lis[0])

    for i in lis:
        if len(max) < len(i):
            max = i
            size = len(max)

    return max,size       


userstring = input("enter your list of words")
lis = userstring.split(' ')
print("your list of words are",lis)

max, size = length(lis)
print("longest word in your list is=",max,"and its size =",size)
