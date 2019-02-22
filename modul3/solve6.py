size = int(input("Masukkan size: "))
z = ""
for num in range(size):
    for num1 in range(0,size-1-num):
        z += "   "
    for num2 in range((num*2)+1):
        z += " * "
    z += "\n"

print(z)