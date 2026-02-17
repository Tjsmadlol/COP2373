# Import reduce so we can perform calculations across a list

from functools import reduce

# Function to add numbers together (used for total)
def add(total, value):
    return total + value

# Function to find which index has the higher expense amount
def higher_index(i, j, amounts):
    if amounts[i] > amounts[j]:
        return i
    else:
        return j

# Function to find which index has the lower expense amount
def lower_index(i, j, amounts):
    if amounts[i] < amounts[j]:
        return i
    else:
        return j


# --- Main Program Starts Here ---

# Lists to store the expense names and their amounts
expense_types = []
expense_amounts = []

# Keep asking the user for expenses until they type 'done'
while True:
    exp_type = input("Enter expense type (or 'done' to finish): ")

    # Stop the loop if the user is finished
    if exp_type.lower() == "done":
        break

    # Ask for the amount of the expense
    amount = float(input("Enter amount: "))

    # Store the type and amount in matching lists
    expense_types.append(exp_type)
    expense_amounts.append(amount)

# Check if the user entered any expenses
if len(expense_amounts) == 0:
    print("No expenses entered.")
else:
    # Use reduce to calculate the total of all expenses
    total = reduce(add, expense_amounts, 0)

    # Create a list of index positions (0, 1, 2, 3, etc.)
    indices = list(range(len(expense_amounts)))

    # Use reduce to find the index of the highest expense
    high_i = reduce(lambda i, j: higher_index(i, j, expense_amounts), indices)

    # Use reduce to find the index of the lowest expense
    low_i = reduce(lambda i, j: lower_index(i, j, expense_amounts), indices)

 # Display the results
    print("\nExpense Summary")
    print("----------------------")
    print(f"Total Expenses: ${total:.2f}")

    # Show the name and amount of the highest expense
    print(f"Highest Expense: {expense_types[high_i]} - ${expense_amounts[high_i]:.2f}")

    # Show the name and amount of the lowest expense
    print(f"Lowest Expense: {expense_types[low_i]} - ${expense_amounts[low_i]:.2f}")