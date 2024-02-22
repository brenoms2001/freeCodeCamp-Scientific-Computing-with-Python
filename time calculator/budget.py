class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = list()
        self.funds = 0
        self.withdraws = 0

    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description' : description})
        self.funds += amount

    def withdraw(self, amount, description = ''):
        if not self.check_funds(amount):
            return False
        self.ledger.append({'amount' : -amount, 'description' : description})
        self.funds -= amount
        self.withdraws += amount
        return True

    def get_balance(self):
        return self.funds

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f"Transfer to {category.name.title()}")
        category.deposit(amount, f"Transfer from {self.name.title()}")
        return True

    def check_funds(self, amount):
        if amount > self.funds:
            return False
        return True

    def __str__(self):
        description = self.name.center(30, "*")
        for flow in self.ledger:
            temp = str(float(flow['amount']))
            if temp[-3] != '.':
                temp += '0'
            if len(temp) >= 7:
                line = f"\n{flow['description'][:22].ljust(22)} {temp.rjust(6)}"
            else:
                line = f"\n{flow['description'][:23].ljust(23)} {temp.rjust(6)}"
            description = description + line
        description = description + f"\nTotal: {self.funds:.2f}\n"
        return description

def create_spend_chart(categories):
    if len(categories) > 4:
        return False
    
    total_withdraw = 0

    for category in categories:
        total_withdraw += category.withdraws

    chart = ''
    for i in range(100, -10, -10):
        chart += f"{i:3}| "
        for category in categories:
            if (category.withdraws/total_withdraw)*100 > i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    chart += "    -" + "-" * (len(categories) * 3) + "\n"
    
    biggest_lenght = 0
    for category in categories:
        if len(category.name) > biggest_lenght:
            biggest_lenght = len(category.name)
    for category in categories:
        if len(category.name) < biggest_lenght:
            difference = biggest_lenght - len(category.name)
            category.name += ' ' * difference

    for i in range(0, biggest_lenght):
        chart += " " * 5
        for category in categories:
            if category.name[i]:
                chart += category.name[i] + "  "
            else:
                chart += "   "
        chart += "\n"
    chart = chart[:-2]
    return chart
