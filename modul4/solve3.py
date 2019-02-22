list1 = [40,100,1,5,25,10]
maxval = list1[0]
minval = list1[0]

for i in range(0,6,1):
    maxval = max(maxval,list1[i])
    minval = min(minval,list1[i])
print("max :",maxval)
print("min :",minval)