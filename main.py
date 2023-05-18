ten = 0
fifty = 0
money = 0
change = 0
water = 200
milk = 200
coffe_beans = 100
while water != 0 and milk != 0 and coffe_beans != 0:
    coffe_type = input("What would you like to have? (espresso/latte/cappuccino )")


    def take_money():
        global ten, fifty, money, change
        print("Please insert coins")
        ten = int(input("How many 10rs coins?: "))
        fifty = int(input("How many 50s notes?: "))
        money = ten * 10 + fifty * 50
        change = money - 100


    def decrease_resources(given_order):
        global water, coffe_beans, milk
        if given_order == "espresso":
            water -= 50
            coffe_beans -= 20
            milk -= 0
        elif given_order == "latte":
            water -= 20
            coffe_beans -= 24
            milk -= 150
        elif given_order == "cappuccino":
            water -= 250
            coffe_beans -= 24
            milk -= 100


    if coffe_type == "espresso":
        if water >= 50 and coffe_beans >= 18:
            take_money()
            if money >= 100:
                print("Here is your change Rs" + str(change))
                decrease_resources(coffe_type)
                print("Here is your espresso!Enjoy!")
            else:
                print("Not enough money! Here is your refund Rs" + str(money))

        else:
            print("sorry! resources not sufficient")
    elif coffe_type == "latte":
        if water >= 0 and coffe_beans >= 24 and milk >= 150:
            take_money()
            if money >= 150:
                print("Here is your change Rs" + str(change))
                decrease_resources(coffe_type)
                print("Here is your espresso!Enjoy!")
            else:
                print("Not enough money! Here is your refund Rs" + str(money))
        else:
            print("sorry! resources not sufficient")
    elif coffe_type == "cappuccino":
        if water >= 0 and coffe_beans >= 24 and milk >= 150:
            take_money()
            if money >= 200:
                print("Here is your change Rs" + str(change))
                decrease_resources(coffe_type)
                print("Here is your espresso!Enjoy!")
            else:
                print("Not enough money! Here is your refund Rs" + str(money))
        else:
            print("sorry! resources not sufficient")
    elif coffe_type == "report":
        print("water: " + str(water) + "ml")
        print("milk: " + str(milk) + "ml")
        print("coffe_beans: " + str(coffe_beans) + "g")

    ten = 0
    fifty = 0
    money = 0
    change = 0
