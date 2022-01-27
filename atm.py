class Atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def balanceinquiry(self):
        print("Your balance is 100 Rs")

    def cashwidthdrawal(self,amount):
        newAmount = 100-amount
        print("You withdrawed : " + str(amount) + "Your balance is : " + str(newAmount))

def main():
    name = input("Whait is your name")
    print("Hello " + name)
    cardnumber = input("Insert your cardnumber : ")
    pin = input("Enter your pin : ")
    new_user = Atm(cardnumber,pin)

    print("Chose your activity")
    print("1. Balance Inquiry")
    print("2. Cash Withdrawal")
    activity = int(input("Enter activity(1 or 2) : "))

    if(activity == 1):
        new_user.balanceinquiry()
    elif(activity == 2):
        amount = int(input("Enter the amount : "))
        new_user.cashwidthdrawal(amount)
    else:
        print("Enter a valid number")

if __name__ == "__main__":
    main()
