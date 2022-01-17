def pattern(row):
    for i in range(1, row+1):
        print(" ")
        for j in range(1, i+1):
            print(i * j, end = " ")
    
row = int(input("enter number of rows"))
pattern(row)        