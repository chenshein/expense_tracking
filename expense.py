class Expense:
    def __init__(self,category, description,amount, date):
        self.description= description
        self.category= category
        self.amount= amount
        self.date = date
    
    def __repr__(self):
        return f"<Expense:{self.category}, {self.description}, {self.amount:.2f}$, {self.date}>"