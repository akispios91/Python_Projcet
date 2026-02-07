import random

def get_secret_number():
    secret = random.randint(1,100)
    return secret



def get_guess():
    
     guess = int(input("pick a number from 1-100: "))
     while True:
          if guess <= 0 or guess > 100:
               guess = int(input("pick a number from 1-100: "))
          else:
               break
     
     return guess


def check_guess(secret, guess):
     if guess == secret:
          print("To Vrikes!!!")
          return True
     elif guess > secret:
          print("eise epanw")
          return False
     else:
          print("eise katw")
          return False
     
def play_game():
     secret = get_secret_number()
     while True:
      guess = get_guess()
      result =  check_guess(guess,secret)
      if result:
           break
      
play_game()
      
     



