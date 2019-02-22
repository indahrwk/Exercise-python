def fibo(urut):
    listdata = [1,1]
    for i in range(2,urut):
        listdata.append(listdata[i-2]+listdata[i-1])
    return listdata[urut-1]
print(fibo(8))