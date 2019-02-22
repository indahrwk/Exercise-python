import math
def reverselist(thelist):
    for i in range(0,math.floor(len(thelist)/2)):
        templist = thelist[i]
        thelist[i] = thelist[len(thelist)-1-i]
        thelist[len(thelist)-1-i] = templist
    return thelist
print(reverselist([1,2,3,4,5,6,7,8]))
