class Expense:
    def __init__(self,category, description,amount):
        self.description= description
        self.category= category
        self.amount= amount
    
    def __repr__(self):
        return f"<Expense:{self.category}, {self.description}, {self.amount:.2f}$>"