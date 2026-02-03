# Name Timothy Strong
# Date January 15, 2026
# Program Ticket Sales

# total tickets
Max_Tickets = 10
# constant to be adhered to
MAX_PER_BUYER = 4

def sell_tickets():
    """
      Manages the ticket selling process.

      Parameters:
      None

      Variables:
      tickets_remaining (int): Accumulator tracking remaining tickets.
      buyer_count (int): Accumulator tracking number of buyers.
      tickets_requested (int): Number of tickets requested by the user.

      Logic:
      1. Initialize tickets_remaining to 10.
      2. Initialize buyer_count to 0.
      3. Loop while tickets_remaining > 0.
      4. Prompt user for number of tickets.
      5. Validate input using if statements.
      6. Subtract tickets from remaining tickets if valid.
      7. Increment buyer counter.
      8. When all tickets sold, call display_total_buyers.

      Return:
      None
      """
    tickets_remaining = Max_Tickets
    buyer_count = 0

    # loops until the tickets are all sold
    while tickets_remaining > 0:
        print(f"\nTickets remaining: {tickets_remaining}")

        tickets_requested = int(input("How many tickets would you like to purchase today? "))

        # valid request
        if tickets_requested < 1 or tickets_requested > MAX_PER_BUYER:
            print("You may only buy between 1 and 4 tickets.")
        elif tickets_requested > tickets_remaining:
            print("Not enough tickets remain for this purchase.")
        else:
            tickets_remaining -= tickets_requested
            buyer_count += 1
            print(f"Successful Purchase. Tickets remaining: {tickets_remaining}")

    display_total_buyers(buyer_count)

def display_total_buyers(buyer_count):
    """
        Displays the total number of buyers after all tickets are sold.

        Parameters:
        buyer_count (int): Total number of buyers.

        Variables:
        None

        Logic:
        1. Display a message indicating all tickets are sold.
        2. Display the total number of buyers.

        Return:
        None
        """
    print("\nAll tickets have been sold!")
    print(f"Overall total number of buyers: {buyer_count}")

# Calls the main ticket sales function
if __name__ == "__main__":
    sell_tickets()