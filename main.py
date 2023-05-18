ten = 0
fifty = 0

water = 200
milk = 200
coffe_beans = 100
while water != 0 and milk != 0 and coffe_beans != 0:
    coffe_type = input("What would you like to have? (espresso/latte/cappuccino )")

    if coffe_type == "espresso":
        if water >= 50 and coffe_beans >= 18:
            print("Please insert coins")
            ten = int(input("How many 10rs coins?: "))
            fifty = int(input("How many 50s notes?: "))
            money = ten * 10 + fifty * 50
            change = money - 100
            if money >= 100:
                print("Here is your change Rs" + str(change))
                water -= 50
                coffe_beans -= 20
                milk -= 0
                print("Here is your espresso!Enjoy!")
            else:
                print("Not enough money! Here is your refund"+str(money))

        else:
            print("sorry! resources not sufficient")
    elif coffe_type == "latte":
        if water >= 0 and coffe_beans >= 24 and milk >= 150:
            print("Please insert coins")
            ten = int(input("How many 10rs notes?: "))
            fifty = int(input("How many 50s notes?: "))
            money = ten * 10 + fifty * 50
            change = money - 150
            if money >= 150:
                print("Here is your change Rs" + str(change))
                water -= 20
                coffe_beans -= 24
                milk -= 150

                print("Here is your espresso!Enjoy!")
            else:
                print("Not enough money! Here is your refund"+str(money))
        else:
            print("sorry! resources not sufficient")
    elif coffe_type == "cappuccino":
        if water >= 0 and coffe_beans >= 24 and milk >= 150:
            print("Please insert coins")
            ten = int(input("How many 10rs notes?: "))
            fifty = int(input("How many 50s notes?: "))
            money = ten * 10 + fifty * 50
            change = money - 200
            if money >= 200:
                print("Here is your change Rs" + str(change))

                water -= 250
                coffe_beans -= 24
                milk -= 100
                print("Here is your espresso!Enjoy!")
            else:
                print("Not enough money! Here is your refund"+str(money))
        else:
            print("sorry! resources not sufficient")
    elif coffe_type == "report":
        print("water: " + str(water) + "ml")
        print("milk: " + str(milk) + "ml")
        print("coffe_beans: " + str(coffe_beans) + "g")
