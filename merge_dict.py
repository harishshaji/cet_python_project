def new_dict():
    limit=int(input("enter no of elements"))
    a={}
    for i in range(0,limit):

        key=input("enter key")
        value=input("enter value")
        a[key]=value
    return a
print("enter the first dictionary")
dict1=new_dict()
print("enter the second dictionary")
dict2=new_dict()
def merge(dict1,dict2):
    return(dict1.update(dict2))
merge(dict1,dict2)
print("the dictionary after merging",dict1)    
