print("Expense Tracker")

expenses = []




while True:
     choice = input("1 Add An expense\n2. View All\n3. Total\n4.Total By Category\n5. Save And Exit\n")

     if choice == "1":
          newexpense = []
          item = float(input("add price: "))
          newexpense.append(item)         
          item = input("Add category: ")
          item.lower()
          item.strip()
          newexpense.append(item)
          item = input("Add description: ")
          newexpense.append(item)
          expenses.append(newexpense)
     elif choice == "2":
          for item in expenses:
              for i, expense in enumerate(expenses, start=1):
               print(f"{i}. {expense[2]} ({expense[1]}) - {expense[0]:.2f} €")
          
          
     elif choice == "3":
         total_amount = sum(expense[0] for expense in expenses)
         print(f"Total expenses: {total_amount:.2f} €")
     elif choice == "4":
        
        category_totals = {}

        for expense in expenses:
          amount = expense[0]
          category = expense[1]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

        for category, total in category_totals.items():
         print(f"{category}: {total:.2f} €")
     elif choice == "5":
          
          break
     
     else:
      print("Wrong Choice Please Try Again")
      choice = input("1 Add An expense\n.2 View All\n.3 Total\n.4 Total By Category\n.5 Save And Exit")

     
     