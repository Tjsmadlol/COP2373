def calculate_discount(price, discount_rate):
    return price * discount_rate


def apply_discount(price, discount_amount):
    return price - discount_amount


def main():
    products = [
        {"name": "Laptop", "price": 1000, "discount_rate": 0.1},
        {"name": "Smartphone", "price": 800, "discount_rate": 0.15},
        {"name": "Tablet", "price": "five hundred", "discount_rate": 0.2},
        {"name": "Headphones", "price": 200, "discount_rate": 0.05}
    ]

    for product in products:
        name = product["name"]

        try:
            price = float(product["price"])
            discount_rate = float(product["discount_rate"])

            discount_amount = calculate_discount(price, discount_rate)
            final_price = apply_discount(price, discount_amount)

            print(f"Product: {name}")
            print(f"Original Price: ${price}")
            print(f"Discount Amount: ${discount_amount}")
            print(f"Final Price: ${final_price}")
            print()

        except (ValueError, TypeError):
            print(f"Error: Invalid price or discount rate for {name}.")
            print("Skipping this product.\n")


if __name__ == "__main__":
    main()


