def times2(num):
    return num*2

listnum = [1,2,3,4,5]
listnum = [times2(item) for item in listnum]
print(listnum)