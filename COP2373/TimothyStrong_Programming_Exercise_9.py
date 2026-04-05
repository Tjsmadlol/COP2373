class BankAcct:
    # This class represents a simple bank account

    def __init__(self, name, account_number, amount, interest_rate):
        # Store basic account info
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    def adjust_interest_rate(self, new_rate):
        # Change the interest rate
        self.interest_rate = new_rate

    def deposit(self, amount):
        # Add money to the account
        if amount > 0:
            self.amount = self.amount + amount
        else:
            print("Deposit must be greater than 0")

    def withdraw(self, amount):
        # Take money out of the account
        if amount > 0 and amount <= self.amount:
            self.amount = self.amount - amount
        else:
            print("Invalid withdrawal")

    def get_balance(self):
        # Return the current balance
        return self.amount

    def calculate_interest(self, days):
        # Calculate simple interest based on number of days
        interest = self.amount * self.interest_rate * (days / 365)
        return interest

    def __str__(self):
        # Display account info
        return ("Name: " + self.name +
                "\nAccount Number: " + str(self.account_number) +
                "\nBalance: $" + str(round(self.amount, 2)) +
                "\nInterest Rate: " + str(self.interest_rate))

# Test function
def test_account():
    # Create a test account
    acct = BankAcct("Tim", 12345, 1000, 0.05)

    print("Starting Account:")
    print(acct)
    print()

    # Test deposit
    acct.deposit(200)
    print("After deposit:")
    print(acct.get_balance())
    print()

    # Test withdrawal
    acct.withdraw(100)
    print("After withdrawal:")
    print(acct.get_balance())
    print()

    # Test interest rate change
    acct.adjust_interest_rate(0.07)
    print("New interest rate:")
    print(acct.interest_rate)
    print()

    # Test interest calculation
    interest = acct.calculate_interest(30)
    print("Interest for 30 days:")
    print(round(interest, 2))
    print()

    # Final account display
    print("Final Account:")
    print(acct)


# Run the test
test_account()