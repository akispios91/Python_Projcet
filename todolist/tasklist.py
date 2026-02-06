
tasklist = []
try:
    with open("C:/Users/akisp/Desktop/todolist/tasklist.txt", "r", encoding="utf-8") as f:
        for line in f:
            tasklist.append(line.strip())
except FileNotFoundError:
     tasklist = []

print("Welcome to To Do list app")



while True:

    choice = input ("1.add task\n2.view task\n3.Delete task\n4.")

    if choice == "1":
        task = input("Enter Task: ")
        task = task.lower()
        tasklist.append(task)
        

    elif choice == "2":
        print(tasklist)

    elif choice == "3":
         Dtask = input("Delete task: ")
         Dtask = Dtask.lower()
         if Dtask in tasklist:
                 tasklist.remove(Dtask)
                 print("Succes Remove")
         else:
              print("task not fount")
                 

    elif choice == "4": 
     with open("C:/Users/akisp/Desktop/todolist/tasklist.txt", "w", encoding="utf-8") as f:
        for task in tasklist:
            f.write(task + "\n")
              
        
     break
    


    else:
     print("Wrong Choice try again")
     choice = input ("1.add task\n2.view task\3.Delete task\4.")

        
    
                 

