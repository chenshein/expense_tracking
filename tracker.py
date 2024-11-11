import calendar
import datetime
from expense import Expense


def main():
    expense_file = "expenses.csv"
    while True:
        print("\nExpense Tracker Menu: 📋")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Get Summary")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice== '1': 
            add_expense(expense_file)
        elif choice == '2':
            view_expense()
        elif choice== '3':
            get_summary()
        elif choice == '4':
            print("BYEEEEE")
            break
        else:
             print("Invalid choice, please try again.")

categories=[
    "Food",
    "Transportation",
    "Health",
    "Housing",
    "Fun",
    "Clothing",
]

def choose_category():
    while True:
        print("🎯 Enter a number or type a custom category: ")
        for i, category in enumerate(categories, start=1):
            print(f"{i}. {category}")
        choice = input()
        if choice.isdigit():
            if 1 <= int(choice) <= len(categories):
                return categories[int(choice) - 1]
            print("❌ Invalid number, please choose again!\n")
            continue
        else:
            categories.append(choice)
            return choice


def validate_date():
    while True:
        date = input("Enter date (YYYY-MM-DD): ")
        try:
            # Validate date format
            date = datetime.datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            continue

def get_user_expense():
    choosen_category = choose_category()
    print(choosen_category)
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


def view_expense():
    pass
def get_summary():
    pass

if __name__ == "__main__" :
    main()


