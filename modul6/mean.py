x = [1,2,3,2,5,2,7,2]

def getmean(list):
    sum = 0
    for item in list :
        sum += item
    mean = sum / len(list)
    return mean
print(getmean(x))