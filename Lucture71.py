menulist = []
pricelist = []


def showbill():
    total = 0
    print("------my food------")
    for number in range(len(menulist)):
        print(menulist[number],pricelist[number])
    total = total + int(pricelist[number])
    print(total,"THB")

while True:
    menuname = input("Menu:")
    if menuname.lower() == "exit":
        break
    else:
        menuprice = input("Price")
        menulist.append(menuname)
        pricelist.append(menuprice)
# print("เมนูที่เลือก",menulist)
# print("ราคา",pricelist)


#     print(menulist[0],pricelist[0])
#     print(menulist[1], pricelist[1])
#     print(menulist[2], pricelist[2])
showbill()