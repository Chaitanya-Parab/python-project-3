class ExpenseTracker:
    def __init__(self):
        self.balance = 0.0
        self.expenses = []

    def add_expense(self, amount, category, description):
        self.expenses.append({
            'amount': amount,
            'category': category,
            'description': description
        })
        self.balance -= amount

    def income(self, amount):
        self.balance += amount

    def view_expenses(self):
        print("Expense List:")
        for expense in self.expenses:
            print(f"Amount: Rs.{expense['amount']}, Category: {expense['category']}, Description: {expense['description']}")

    def current_balance(self):
        print(f"Your current balance is Rs.{self.balance:.2f}")


# Example usage:
tracker = ExpenseTracker()

# Adding expenses
tracker.add_expense(50.0, 'Food', 'Lunch and Dinner everyday')
tracker.add_expense(20.0, 'Transport', 'Taxi')
tracker.add_expense(40.0, 'Entertainment', 'TV')
tracker.add_expense(20.0, 'Grocery', 'Everyday home need such as vegetables,bakery etc')
tracker.add_expense(30.0, 'Light Bill', 'Fan and Electricity used everyday')


# Adding income
tracker.income(1000.0)

# Viewing expenses and balance
tracker.view_expenses()
tracker.current_balance()
