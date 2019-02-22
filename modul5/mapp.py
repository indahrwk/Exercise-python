# def times2(num):
#     return num * 2
# listnum = [1,2,3,4,5]
# listnum = list(map(times2,listnum))
# print(listnum)

listnum = [1,2,3,4,5]
listnum = list(map(lambda num : num * 2,listnum))
print(listnum)