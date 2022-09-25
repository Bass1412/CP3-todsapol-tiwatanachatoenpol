menulist = []
def showbill():
    total = 0
    print("------my food------")
    for number in range(len(menulist)):
        print(menulist[number])
        total = total + int(menulist[number][1])
        print(total)
while True:
    menuname = input("Menu:")
    if menuname.lower() == "exit":
        break
    else:
        menuprice = input("Price")
        menulist.append([menuname,menuprice])

showbill()