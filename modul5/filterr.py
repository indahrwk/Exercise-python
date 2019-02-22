# def genap(num):
#     return num % 2 == 0
# listnum = [1,2,3,4,5]
# listnum = list(filter(genap,listnum))
# print(listnum)

##filter withnlambda

listnum = [1,2,3,4,5]
listnum = list(filter(lambda num : num % 2 == 0,listnum))
print(listnum)