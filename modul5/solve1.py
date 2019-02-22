# x1 = input("masukkan kata :")
# x2 = input("masukkan kata :")
# list1 = ['Merdeka','Hello','Hellos','Sohib','Kari ayam']

# check1 = 'ka' in 'Merdeka','Kari ayam'
# check2 = 'hel' in 'Hello','Hellos'

# print(x1,check1)
# print(x2,check2)

listdata = ['Merdeka','Hello','Hellos','Sohib','Kari ayam']
print(listdata)
inputuser = input("masukkan kata : ")

def searchlist(keyword,thelist):
    newlist = list(filter(lambda item : keyword.lower() in item.lower(),thelist))
    return newlist

searchedlist = searchlist(inputuser,listdata)
print(searchedlist)

