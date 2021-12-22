string = input("enter a string")
count =0
string = list(string)
for i,n in enumerate(string):
	if n == string[0]:
		count+=1
		if count > 1:
			string[i] = "$"
string = "".join(string)
print("new string:",string)
		
 
	
	

