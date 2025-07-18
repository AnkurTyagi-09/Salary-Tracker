print("Salary Tracker")

import os
import csv
import getpass
FILE_NAME = "salary.csv"
PASSWORD = "1234"  # Replace with your desired password

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Name", "Amount", "Category", "Designation"])

def authenticate():
    user_password = getpass.getpass("Enter password to access Salary Tracker: ")
    if user_password == PASSWORD:
        print("Access granted.")
        return True
    else:
        print("Access denied.")
        return False

def add_expense():
    Date = input("Enter the date (YYYY-MM-DD): ")
    Name = input("Enter the name: ")
    
    while True:
        Amount = input("Enter the amount: ")
        try:
            Amount = float(Amount)  
            break
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
    
    while True:
        Category = input("Enter the category (Expense/Revenue): ").capitalize()
        if Category in ["Expense", "Revenue"]:
            break
        else:
            print("Invalid category. Please enter 'Expense' or 'Revenue'.")
    
    Designation = input("Enter the designation: ")

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([Date, Name, Amount, Category, Designation])

    print("Expense added successfully.")

def view_expenses():
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            if len(row) == 5:  
                print(f"Date: {row[0]}, Name: {row[1]}, Amount: {row[2]}, Category: {row[3]}, Designation: {row[4]}")
                print()  

def delete_expense():
    date = input("Enter the date of the expense to delete (YYYY-MM-DD): ").strip()
    name = input("Enter the name of the expense to delete: ").strip()

    rows = []
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        deleted = False
        for row in rows:
            if row and row[0] == date and row[1] == name:  
                deleted = True
                continue
            writer.writerow(row)

    if deleted:
        print("Expense deleted successfully.")
    else:
        print("Expense not found.")

def calculate_totals():
    expenses_total = 0.0
    revenue_total = 0.0

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            if row and len(row) == 5:  
                try:
                    Amount = float(row[2])
                    if row[3].lower() == "expense":
                        expenses_total += Amount
                    elif row[3].lower() == "revenue":
                        revenue_total += Amount
                except ValueError:
                    pass  

    return expenses_total, revenue_total

def generate_trial_balance():
    expenses_total, revenue_total = calculate_totals()
    print("\nTrial Balance Sheet")
    print("-------------------")
    print(f"Total Expenses: {expenses_total}")
    print(f"Total Revenue: {revenue_total}")
    print(f"Net Total: {revenue_total - expenses_total}")

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Generate Trial Balance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            delete_expense()
        elif choice == '4':
            generate_trial_balance()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    if authenticate():
        main()