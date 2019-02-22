# x = [6000,34,203,3,746,200,984,198,764,9,1]

# def bubblesort(list):
#     for i in range(len(list),0,-1):
#         for j in range(0,i-1):
#             if(list[j] > list[j+1]):
#                 temp = list[j]
#                 list[j] = list[j+1]
#                 list[j+1]=temp
#     return list
# print(bubblesort(x))

def bubblesort(arr):
    n = len(arr)
    for i in range(n): 
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:  
               arr[j], arr[j+1] = arr[j+1],arr[j]
arr = [6000,34,203,3,746,200,984,198,764,9,1]
# arr1 = [34,203,3,746,200,984,198,764,9,1,6000]
# arr2 = [34,3,203,746,200,984,198,764,9,1,6000]
# arr3 = [34,3,203,200,746,984,198,764,9,1,6000]
# arr4 = [34,3,203,200,746,198,984,764,9,1,6000]
# arr5 = [34,3,203,200,746,198,764,9,1,984,6000]
# arr6 = [34,3,203,200,746,198,9,1,764,984,6000]
# arr7 = [34,3,203,200,198,9,1,746,764,984,6000]
# arr8 = [1,3,9,34,198,200,203,746,764,984,6000]
bubblesort(arr)
print("sorted array is : ")
for i in range (len(arr)):
    print("%d" %arr[i])
    
