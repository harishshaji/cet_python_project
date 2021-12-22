st1 = input("enter first string")
st2 = input("enter second string")
st1 = list(st1)
st2 = list(st2)
st1[0],st2[0] = st2[0],st1[0]
st1 = "".join(st1)
st2 = "".join(st2)
st1 = st1+" "+st2
print(st1)
