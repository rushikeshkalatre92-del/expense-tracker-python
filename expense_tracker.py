expenses = []

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter expense name: ")
        amount = float(input("Enter amount: "))

        expense = {
            "item": item,
            "amount": amount
        }

        expenses.append(expense)
        print("Expense added successfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses found.")
        else:
            print("\nExpense List:")
            for expense in expenses:
                print(expense)

    elif choice == "3":
        total = 0
        for expense in expenses:
            total += expense["amount"]

        print("Total Expense =", total)

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")