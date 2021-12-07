def new_dict():
    limit=int(input("enter no of elements"))
    a={}
    for i in range(0,limit):

        key=input("enter key")
        value=input("enter value")
        a[key]=value
    return a
dict1 = new_dict()
print(dict1)
print("ascending order:",sorted(dict1.items()))       
print("decending order:",sorted(dict1.items(),reverse=True))        