import json
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
   while True:
    try:
     choice = int(input("1.Balance\n2.Deposit\n3.Withdraw\n4.Exit\n"))
     if 1 <= choice <= 4:
        return choice

    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
    


def show_balance(balance):
    print("Your Balance is: " ,balance)


def deposit(balance):
  while True:
   try:
    money = int(input("Amount of Deposit: "))
    if money > 0:
      balance = money + balance
      return balance
    else:
     print("Give me Positive Number")
   except ValueError:
        print("Invalid input. Please enter a valid amount.")
        

def withdraw(balance):
    while True:
     try:
      amount = int(input("Amount of Withdraw: "))
      if amount > balance or amount <= 0:
        print("Invalid amount of money")
        
      else:
        balance = balance - amount
        print("Your new balance is: " ,balance)

        return balance
     except ValueError:
       print("Enter a Valid Number")


def load_data():
    try:
        with open("atm_data.json", "r") as f:
            data = json.load(f)      # 1) διάβασε JSON → dict
            return data["balance"]   # 2) πάρε το balance και γύρνα το
    except FileNotFoundError:
        return 1000                 # αν δεν υπάρχει αρχείο, default
    
import json

def save_data(balance):
    # 1) Φτιάχνουμε dict με ΤΟ ΙΔΙΟ key που διαβάζουμε στο load
    data = {
        "balance": balance
    }

    # 2) Ανοίγουμε το αρχείο σε write mode ("w")
    # Αν δεν υπάρχει, θα δημιουργηθεί
    # Αν υπάρχει, θα αντικατασταθεί
    with open("atm_data.json", "w") as f:
        # 3) Γράφουμε το dict σαν JSON μέσα στο αρχείο
        json.dump(data, f)

mypin = 1234

ok = login(mypin)

if ok == False:
    print("Access Denied")
    

else:
    balance = load_data()
    while True:

     choice = show_menu()
     if choice == 1:
      show_balance(balance)
     elif choice == 2:
      balance = deposit(balance)
      save_data(balance)
     elif choice == 3:
      balance = withdraw(balance)
      save_data(balance)
     elif choice == 4:
        print("Success Exit")
        break
    
        
         
         



    
