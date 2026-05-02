import json
from datetime import datetime

FILE_NAME = "expenses.json"

def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []

def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD) or press Enter: ")

    if date == "":
        date = str(datetime.today().date())

    expenses = load_expenses()
    expenses.append({"amount": amount, "category": category, "date": date})
    save_expenses(expenses)
    print("Expense added!")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found")
        return
    for i, e in enumerate(expenses, 1):
        print(i, e["date"], e["category"], e["amount"])

def delete_expense():
    expenses = load_expenses()
    view_expenses()
    try:
        idx = int(input("Enter number to delete: "))
        if 1 <= idx <= len(expenses):
            expenses.pop(idx-1)
            save_expenses(expenses)
            print("Deleted successfully")
    except:
        print("Invalid input")

def category_summary():
    expenses = load_expenses()
    summary = {}
    for e in expenses:
        summary[e["category"]] = summary.get(e["category"], 0) + e["amount"]
    print(summary)

def monthly_summary():
    month = input("Enter month (YYYY-MM): ")
    expenses = load_expenses()
    total = 0
    for e in expenses:
        if e["date"].startswith(month):
            total += e["amount"]
            print(e)
    print("Total:", total)

def menu():
    while True:
        print("\n1.Add 2.View 3.Delete 4.Category 5.Monthly 6.Exit")
        c = input("Choice: ")
        if c == "1":
            add_expense()
        elif c == "2":
            view_expenses()
        elif c == "3":
            delete_expense()
        elif c == "4":
            category_summary()
        elif c == "5":
            monthly_summary()
        elif c == "6":
            break

menu()
