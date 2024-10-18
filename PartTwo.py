print("This machine accepts 50p, 20p, 10p and 5p coins. ")
print("The drink costs £1. ")
due1 = 100
money1 = 0
while money1 < due1:
    money2 = int(input("Please insert coins one at a time. "))
    if money2 != 50 and money2 != 20 and money2 != 10 and money2 != 5:
        print("This machine does not accept that type of coin. ")
    else:
        money1 = money1 + money2
        if money1 < due1:
            print("You have inserted", money1, "\nYou need to insert", due1 - money1, "more. ")
        elif money1 == due1:
            print("You have payed for your drink, Enjoy. ")
        else:
            change = money1 - due1
            print("You are owed", change, "in change. ")
