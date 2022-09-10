usernameinput = input("Username:")
passwordinput = input("Password:")

if usernameinput == "Admin1234" and passwordinput == "1234567" :
    print("login success")
    print("1: coffe 55 THB")
    print("2: Tea 45 THB")
    user_buy_product = int(input("กรุณาเลือกสินค้า"))
    if user_buy_product == 1:
        unit_buy = int(input("1 กรุณาใส่จำนวนที่ต้องการ"))
        print("ราคา :" , 55 * unit_buy , "THB")
    elif  user_buy_product == 2:
          unit_buy2 = int(input("2 กรุณาใส่จำนวนที่ต้องการ"))
          print("ราคา :", 45 * unit_buy2, "THB")

    print("Thank you")
else:
    print("login Fell")