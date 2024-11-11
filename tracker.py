import os
import datetime
from expense import Expense

RED = "\033[31m"
BLUE = "\033[34m"
DARK_BLUE = "\033[1;34m"
RESET = "\033[0m"
BOLD = "\033[1m"

def main():
    expense_file = "expenses.csv"
    while True:
        print(f"\n{BOLD}Expense Tracker Menu: {RESET}")
        print("1. ➕ Add Expense ")
        print("2. 🔎 View Expenses")
        print("3. 🧾 Get Summary")
        print("4. ❌ Exit")
        choice = input("Choose an option: ")
        if choice== '1': 
            add_expense(expense_file)
        elif choice == '2':
            view_expense(expense_file)
        elif choice== '3':
            get_summary(expense_file)
        elif choice == '4':
            print("Goodbye! 👋")
            break
        else:
             print(f"{RED}❌ Invalid choice, please try again.{RESET}")

# load categories from file
def load_categories():
    categories=[
    "Food",
    "Transportation",
    "Health",
    "Housing",
    "Fun",
    ]
    if os.path.exists('categories.txt'):
        with open('categories.txt', 'r') as file:
            categories = [line.strip() for line in file.readlines()]
    return categories

# Save categories to a file
def save_categories(categories):
    with open('categories.txt', 'w') as file:
        for category in categories:
            file.write(category + '\n')

def choose_category():
    categories = load_categories()
    while True:
        print("🎯 Enter a number or type a custom category: ")
        for i, category in enumerate(categories, start=1):
            print(f"{i}. {category}")
        choice = input()
        if choice.isdigit():
            if 1 <= int(choice) <= len(categories):
                return categories[int(choice) - 1]
            print(f"{RED}❌ Invalid number, please choose again!\n{RESET}")
            continue
        else:
            categories.append(choice)
            save_categories(categories)
            return choice

def validate_date():
    while True:
        date = input("🗓️  Enter date (YYYY-MM-DD): ")
        try:
            # Validate date format
            date = datetime.datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            print(f"{RED}❌ Invalid date format. Please use YYYY-MM-DD.{RESET}")
            continue

def get_user_expense():
    choosen_category = choose_category()
    item_description = input("🎯 Enter item description : ")
    amount = float(input("🎯 Enter item cost (💲): "))
    date = validate_date()
    new_expense = Expense(category = choosen_category,description=item_description,amount=amount,date=date)
    return new_expense

def add_expense(expense_file):
    expense = get_user_expense()
    print(f"🎯 Saving User Expense: {expense} to {expense_file}")
    with open(expense_file, mode='a', newline='', encoding='utf-8') as file:
        file.write(f"{expense.category},{expense.description},{expense.amount},{expense.date}\n")    

def view_expense(expense_file):
    print(f"🎯 View User Expense: ")
    with open(expense_file, mode='r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()  
            if line:  
                print(line)


def amount_per_category(expenses_list):
    amount_by_category={}
    for expense in expenses_list:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    print(f"{DARK_BLUE}Amount by category: {RESET}")
    for key, amount in amount_by_category.items():
        print(f"{BLUE}{key}: {RESET}{amount:.2f}$")



def get_summary(expense_file):
    print("🎯 Summarizing Total User Expense:")
    expenses_list_csv = []  # A list of Object type Expense
    with open(expense_file, mode='r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            category, name, amount,date = line.split(",")
            split_line = Expense(category,name,float(amount),date)
            expenses_list_csv.append(split_line)
        #calculate total amount that spent
        total_spent = sum([expense.amount for expense in expenses_list_csv]) 
        print(f"{DARK_BLUE}Total amount spent: {RESET}{float(amount):.2f}$")
        amount_per_category(expenses_list_csv)

    

if __name__ == "__main__" :
    main()


