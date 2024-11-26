from ast import List
from collections import defaultdict
from expense import Expense
import os
import calendar
import datetime
from datetime import datetime
from datetime import datetime
# i import twice cause why not xdd
from datetime import datetime

now = datetime.now()


def main():
    print(f"running expense tracker")
    expense_files_path = "expenses.csv"

    budget = budget_input() #budget to spend monthly 
    # add a input for your budget once untill the month ends then ask for the budget again when your run it
    expense = get_user_expense()
    # print(expense)

    writing_user_expense(expense, expense_files_path)

    summarize_user_expense(expense_files_path, budget)

    # get user input for budget hopefully its enough for da month
def budget_input():
    while True:
        try:
            print(f"what is your budget?")
            budget_amount = float(input("enter budget: "))
            return budget_amount
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
def get_user_expense():
    print(f"gettin user expense")
    expense_name = input("enter expense name:")
    expense_amount = float(input("enter expense amount:"))
    # print(f"youve entered {expense_name},{expense_amount}")

    expense_categories = ["Food", "Home", "work", "Fun", "misc"]

    while True:
        print("select a catergory: ")
        for i, category_name in enumerate(expense_categories):
            print(f"{i + 1}.{category_name}")

        value_range = f"(1 - {len(category_name)})"
        selected_index = int(input(f"Enter a category {value_range}:")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                name=expense_name, category=selected_category, amount=expense_amount
            )
            return new_expense
        else:
            print("invalid category, try again")

    # write to a file


def writing_user_expense(expense: Expense, expense_file_path):

    # script_dir = os.path.dirname(os.path.abspath(__file__))
    # full_path = os.path.join(script_dir, expense_file_path)
    print(f"saving user expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")


def summarize_user_expense(expense_file_path, budget):
    print(f"summarize user expense")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            strippd_line = line.strip()
            expense_name, expense_amount, expense_category = strippd_line.split(",")
            line_expense = Expense(
                name=expense_name,
                amount=float(expense_amount),
                category=expense_category,
            )
            # print(line_expense)
            expenses.append(line_expense)

    amount_by_Category = {}
    for expense in expenses:
        key = expense.category
        # Initialize defaultdict to handle missing categories automatically
        amount_by_Category = defaultdict(float)
        for expense in expenses:
            amount_by_Category[expense.category] += expense.amount
        # Automatically adds if category doesn't
    for key, amount in amount_by_Category.items():

        print(f"  {key}: ${amount:.2f}")

    total_spent = sum([x.amount for x in expenses])
    print(f"you ve spent: ${total_spent:.2f} this month!")

    remaining_budget = budget - total_spent
    print(f"budget left: ${remaining_budget:.2f} this month!")

    now = datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day
    print("remaining days in the currrent month:", remaining_days)

    daily_budget = remaining_budget /remaining_days
    print(yellow(f"budget per day {daily_budget:.2f}"))


def yellow(text):
    return "\033[33m" + text + "\033[0m"


if __name__ == "__main__":
    main()
