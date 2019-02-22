num = int(input("Enter a number : "))
for i in range(num,0,-1):
    print(" * " * i)
z= ''
for item in range(num-1):
    for item1 in range(0,item+2):
        z += ' * '
    z += '\n'
print(z)