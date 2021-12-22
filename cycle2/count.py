a=input("Enter a line of senetence : ")
word={}
a=a.split(" ")
for i in a : 
	if i not in word.keys() : 
		 word[i] = 1
	else : 
		s=word[i]
		s=s+1
		word[i] = s
for i in word : 
	print(i," : ",word[i])
	
		
