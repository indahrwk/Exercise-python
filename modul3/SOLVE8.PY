size = int(input("Masukkan size: "))
z = ""

for num in range(size):
    for num1 in range(num, size):
        z += " * "
    for num2 in range(0, (num*2)-1):
        z += "   "
    for num3 in range(size, num, -1):
        if(num3 == 1):
            break
        z += " * "
    z += "\n"
for num in range(size-1):
    for num1 in range(0, num+2):
        z += " * "
    for num2 in range(size*2-5, num*2, -1):
        z += "   "
    for num3 in range(0, num+2):
        if(num == size-2 and num3 == num+1):
            break
        z += " * "
    z += "\n"

print(z)