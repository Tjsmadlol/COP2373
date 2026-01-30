#This function calculates the discount amount based on the product price
# and the discount rate provided
def calculate_discount(price, discount_rate):
    # Multiply the price by the discount rate to get the discount amount
    return price * discount_rate


# This function applies the calculated discount to the original price
def apply_discount(price, discount_amount):
    # Subtract the discount amount from the original price
    return price - discount_amount


# The main function controls the execution of the program
def main():
    # A list of dictionaries that store product information
    products = [
        {"name": "Laptop", "price": 1000, "discount_rate": 0.1},
        {"name": "Smartphone", "price": 800, "discount_rate": 0.15},

        # ORIGINAL MISTAKE (explained):
        # The original issue was that the price was entered as "500" (a string).
        # This does NOT actually break the program because float("500") works.
        #
        # INTENTIONAL CHANGE:
        # The value "five hundred" is intentionally incorrect input to
        # demonstrate proper error handling using try/except.
        {"name": "Tablet", "price": "five hundred", "discount_rate": 0.2},

        {"name": "Headphones", "price": 200, "discount_rate": 0.05}
    ]

    # Loop through each product in the list
    for product in products:
        # Extract the product name
        name = product["name"]

        try:
            # Attempt to convert the price to a float
            # This will fail for invalid input like "five hundred"
            price = float(product["price"])

            # Convert the discount rate to a float
            discount_rate = float(product["discount_rate"])

            # Calculate the discount amount
            discount_amount = calculate_discount(price, discount_rate)

            # Calculate the final price after applying the discount
            final_price = apply_discount(price, discount_amount)

            # Display product information
            print(f"Product: {name}")
            print(f"Original Price: ${price}")
            print(f"Discount Amount: ${discount_amount}")
            print(f"Final Price: ${final_price}")
            print()

        except (ValueError, TypeError):
            # This block runs when invalid data is encountered
            # The program continues running instead of crashing
            print(f"Error: Invalid price or discount rate for {name}.")
            print("Skipping this product.\n")


# This ensures the main function runs only when the file is executed directly
if __name__ == "__main__":
    main()


