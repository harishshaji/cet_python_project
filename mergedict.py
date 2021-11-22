dict1 = {'nelwin': 80, 'shifan': 75, 'sreeraj': 60}
dict2 = {'nelwin': 100, 'shifan': 80, 'sreeraj': 80}
dict3 = { }  
  
for key in dict1:
    dict3[key] = dict1[key]
for key in dict2:
    if key in dict3:
        dict3[key] = dict3[key] + dict2[key]
    else:
        dict3[key] = dict2[key]
    
          
print('dictionary after merging',dict3)
print('first dictonary',dict1)
print('second dictonary',dict2)
