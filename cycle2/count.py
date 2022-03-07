str=input("enter a string").split()
word={}
for i in str:
    if i not in word.keys():
        word[i]=1
    else:
        word[i]+=1
for i in word:
    print(word[i]) 
		
