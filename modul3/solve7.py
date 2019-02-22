size = int(input("masukkan size : "))
z = ""
for num in range(size):
    for num1 in range(num):
        z += "   "
    for num2 in range((size*2)-(num*2)-1):
    
        z += " * "
    z += "\n"
print(z)