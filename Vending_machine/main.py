import random

checks = "y"
total_price = 0

menu = {
    1 : {"name" : "Coke", "price" : 15},
    2 : {"name" : "Water", "price" : 10},
    3 : {"name" : "Tea", "price" : 20},
    4 : {"name" : "Green Tea", "price" : 20},
    5 : {"name" : "Coffee", "price" : 20}
}

print("--เมนูเครื่องดื่ม--")
for number , item in menu.items():
    print(f"{number} : {item["name"]} ราคา {item["price"]} บาท")

print("--------------------")

try:
    while checks == "y":
        selection = int(input("ใส่หมายเลขเครื่องดื่ม : "))
        if selection in menu:
            selection_item = menu[selection]
            print(f"คุณเลือกเมนู {selection_item["name"]}")
            print(f"ราคา {selection_item["price"]} บาท")

            many = int(input("ต้องการซื้อจำนวนเท่าไหร่ : "))
            total_item_price = many * selection_item["price"]
            print(f"รวมราคาสินเค้านี้เท่ากับ : {total_item_price} บาท")
            total_price = total_price + total_item_price
            print(f"ยอดรวมสินค้าของคุณตอนนี้คือ {total_price} บาท")
            checks = str(input("ต้องการซื้ออย่างอื่นเพิ่มมั้ย(y/n) : "))
        else:
            print("ใส่ข้อมูลให้ถูกต้อง")
    print(f"คุณต้องจ่ายทั้งหมด {total_price} บาท")

except:
    print("ใส่ข้อมูลไม่ถูกต้อง")
print("------------------")

pay_way = str(input("เลือกช่องทางการจ่ายเงิน(Digital or Cash) : "))

print("------------------")

member = str(input("ท่านเป็นสมาชิกหรือไม่(y/n)"))
if member == "y":
    discout = total_price * (10/100)
    total_price = total_price - discout
    print(f"ท่านเป็นสมาชิกได้ส่วนลด 10%")
    print(f"ยอดเงินที่ต้องจ่ายคงเหลือ {total_price} บาท")
    while True:
        if pay_way.lower() in ["digital","d"]:
            pay = int(input("กรุณาใส่จำนวนเงินที่ต้องจ่าย : "))
            if pay == total_price:
                bill = str(input("รับใบเสร็จมั้ย(y/n) : "))
                if bill == "y":
                    print("สั่งซื้อสำเร็จ")
                    print(f"ยอดสินค้า {total_price} บาท")
                    print(f"คุณจ่าย {pay} บาท")
                    print("ขอบคุณที่ใช้บริการ")
                else:
                    print("ขอบคุณที่ใช้บริการ")
                break
            else:
                print("กรอกจำนวนเงินให้ถูกต้อง และ พอดีกับราคาสินค้า")

        elif pay_way.lower() in ["cash","c"]:
            while True:
                pay = int(input("ใส่จำนวนเงินของคุณ : "))
                change = pay - total_price
                if pay >= total_price:
                    print(f"รับเงินจากคุณมา {pay} บาท")
                    print(f"ทอนเงินทั้งหมด {change} บาท")
                    bill = str(input("รับใบเสร็จมั้ย(y/n) : "))
                    if bill == "y":
                        print("สั่งซื้อสำเร็จ")
                        print(f"ยอดสินค้า {total_price} บาท")
                        print(f"คุณจ่าย {pay} บาท")
                        print(f"ทอนเงิน {change} บาท")
                        print("ขอบคุณที่ใช้บริการ")
                    else:
                        print("ขอบคุณที่ใช้บริการ")
                    break
                elif pay < total_price:
                    print("กรุณาใส่จำนวนให้ครบ")
elif member == "n":
    while True:
        if pay_way.lower() in ["digital","d"]:
            pay = int(input("กรุณาใส่จำนวนเงินที่ต้องจ่าย : "))
            if pay == total_price:
                bill = str(input("รับใบเสร็จมั้ย(y/n) : "))
                if bill == "y":
                    print("สั่งซื้อสำเร็จ")
                    print(f"ยอดสินค้า {total_price} บาท")
                    print(f"คุณจ่าย {pay} บาท")
                    print("ขอบคุณที่ใช้บริการ")
                else:
                    print("ขอบคุณที่ใช้บริการ")
                break
            else:
                print("กรอกจำนวนเงินให้ถูกต้อง และ พอดีกับราคาสินค้า")
        elif pay_way.lower() in ["cash","c"]:
            pay = int(input("ใส่จำนวนเงินของคุณ : "))
            change = pay - total_price
            if pay >= total_price:
                print(f"รับเงินจากคุณมา {pay} บาท")
                print(f"ทอนเงินทั้งหมด {change} บาท")
                bill = str(input("รับใบเสร็จมั้ย(y/n) : "))
                if bill == "y":
                    print("สั่งซื้อสำเร็จ")
                    print(f"ยอดสินค้า {total_price} บาท")
                    print(f"คุณจ่าย {pay} บาท")
                    print(f"ทอนเงิน {change} บาท")
                    print("ขอบคุณที่ใช้บริการ")
                else:
                    print("ขอบคุณที่ใช้บริการ")
                break
            elif pay < total_price:
                print("กรุณาใส่จำนวนให้ครบ")

print("---------------------")

game_check = str(input("ต้องการเล่นเกมหรือไม่(y/n) : "))
if game_check == "y":
    print("เกมทายตัวเลข 1-10")
    number = random.randint(1,10)
    guess = -1
    count = 0
    while guess != number:
        guess = int(input("ทายตัวเลข 1-10 : "))
        count += 1
        if guess > number:
            print("มากไป")
        elif guess < number:
            print("น้อยไป")

    print("----------------------")
    print(f"ถูกต้องคร้าบ คำตอบคือ {number}")
    print(f"คุณใช้ไปทั้งหมด {count} รอบ")