systemMenu = {"ไก่ทอด": 35, "เป็ดทอด": 45, "ปลาทอด": 55, "ผักทอด": 20}
menulist = []
def showbill():
    total = 0
    print("------my food------")
    for number in range(len(menulist)):
        print(menulist[number][0],menulist[number][1])
        total = total + int(menulist[number][1])
        print(total)
while True:
    menuname = input("Menu:")
    if menuname.lower() == "exit":
        break
    else:
        menulist.append([menuname,systemMenu[menuname]])

showbill()