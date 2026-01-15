# Name Timothy Strong

# Date January 15, 2026

# Program Ticket Sales

Max_Tickets = 20
MAX_PER_BUYER = 4

def sell_tickets():
    tickets_remaining = Max_Tickets
    total_buyers = 0

    #loop until the tickets are all sold
    while tickets_remaining > 0:
        print(f"\nTickets remaining: {tickets_remaining}")

        tickets_requested = int(input("How many tickets would you like to buy (1-4)? "))

        #valid request
        if tickets_requested < 1 or tickets_requested > MAX_PER_BUYER:
            print("You may only buy between 1 and 4 tickets.")
        elif tickets_requested > tickets_remaining:
            print("Not enough tickets remain for this purchase.")
        else:
            tickets_remaining -= tickets_requested
            total_buyers += 1
        print(f"Successful Purchase. Tickets remaining: {tickets_remaining}")

    display_total_buyers(total_buyers)

def display_total_buyers(total_buyers):
    print("\n All tickets have been sold!")
    print(f"Overall total number of buyers: {total_buyers}")

#Calling the main ticket sales function
sell_tickets()