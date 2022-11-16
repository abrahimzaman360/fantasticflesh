from random import randint

# Constants
fruitList = ["Oranges", "Apples", "Banana", "Grapes", "Strawberry"]
cart = []
menuInput = [0, 1, 2]
fakecard = {
    "cardnumber": "123-233-648-323",
    "expdate": "06/27",
    "cvc": "107"
}

# Shop Class:
class Shop:
    def __init__(self, flist):
        self.flist = flist
        self.getMenu()

    def getMenu(self):
        from os import system
        system('cls')
        print("Welcome to My Fruit Shop!")
        print("Menu:")
        print("1: Show Available Fruits in Shop.")
        print("2: Show Cart.")
        print("0: Quit. \n")
        menuinp = int(input("Menu: "))
        if menuinp not in menuInput:
            print("Wrong Input")
        elif menuinp == 1:
            self.getFruitList()
        elif menuinp == 2:
            self.cartView()
        elif menuinp == 0:
            exit(1)

    def getFruitList(self):
        print("Fruit List:")
        for i, j in enumerate(zip(self.flist)):
            print(i, j)
        inp = str(
            input("Enter Name of Fruit to Add in Cart or \'q\' for Main Menu:  "))
        if inp in fruitList:
            cart.append(inp)
            print("Added \"{}\" to Cart!".format(inp))
            check = str(input("Enter \'c\' for Cart Checkout: "))
            if check == "c" or check == "C":
                self.cartView()
            else:
                self.getMenu()
        elif inp not in self.flist:
            print("Item not found!")
        elif inp == "q" or inp == "Q":
            self.getMenu()

    def cartView(self):
        if len(cart) <= 0:
            print("Cart is Empty!")
            inp = str(input("\'m\' for Main Menu or \'q\' for Quit Program:  "))
            if inp == "m" or inp == "M":
                self.getMenu()
            elif inp == "q" or inp == "Q":
                exit(1)
        else:
            print("Following Items are in Cart: ")
            for item in enumerate(cart):
                print(item)
            print("\n")
            buyinp = str(input("Enter \'b\' to Any Buy:  "))
            if buyinp == "b" or buyinp == "B":
                whichtoBuy = str(
                    input("Enter Name of Item You Wanna Buy from Cart:  "))
                for item in cart:
                    if whichtoBuy != item:
                        break
                    elif whichtoBuy in cart:
                        name = str(input("Enter Your Name: "))
                        if (len(name) <= 3):
                            self.getMenu()
                        else:
                            print("Item You've Bought Now:\t", whichtoBuy)
                            randp = randint(0, 1000)
                            with open("invoice{}.txt".format(randp), "w") as file:
                                file.write("Invoice Generated: ")
                                file.write("\nBuyer Name: {}".format(name))
                                file.write("\nPayment Done Using Debit Card: ")
                                file.write("\nCard Details: ")
                                file.write("\nCard Number:\t{}".format(
                                    fakecard.get('cardnumber')))
                                file.write("\nDate Expiry:\t{}".format(
                                    fakecard.get('expdate')))
                                file.write("\nCard CVC   :\t{}".format(
                                    fakecard.get('cvc')))
                                file.write(
                                    "\nJunior Programmer:\tIbrahim Zaman!")
                            file.close()
                            print("Check Invoice{}.txt File in Directory!".format(randp))

    def putinCart(self, item):
        if item in self.flist:
            cart.append(item)
            self.cartView(cart)


myShop = Shop(fruitList)
