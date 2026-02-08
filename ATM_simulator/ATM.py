def login(mypin):
    trys = 3
    while trys > 0:
        pin = int(input("Enter Your  Pin:"))
        if pin == mypin:
            print("Welcome Yo your Accoun")
            return True
        else:
            trys -= 1
            print("Wrong Pin Try Again")

    return False



def show_menu():
  
    choice = int(input("1.Balance\n2.Deposit\n3.Withdraw\n4.Exit\n"))

    return choice
    


def show_balance(balance):
    print("Your Balance is: " ,balance)


def deposit(balance):
   money = int(input("Amount of Deposit: "))
   balance = money + balance
   return balance

def withdraw(balance):
    amount = int(input("Amount of Withdraw: "))
    if amount > balance:
        print("Invalid amount of money")
        
    elif amount <= balance:
        balance = balance - amount
        print("Your new balance is: " ,balance)

    return balance


mypin = 1234

ok = login(mypin)

if ok == False:
    print("Access Denied")
    

else:
    balance = 1000
    while True:

     choice = show_menu()
     if choice == 1:
      show_balance(balance)
     elif choice == 2:
      balance = deposit(balance)
     elif choice == 3:
      balance = withdraw(balance)
     elif choice == 3:
        print("Success Exit")
        break
     else:
        print("wrong choice")
        
         
         



    
