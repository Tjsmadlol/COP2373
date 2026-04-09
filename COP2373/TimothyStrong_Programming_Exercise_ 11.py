import random


class Card:
    # This class makes one card
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        # This returns the card as a string
        return self.rank + " of " + self.suit


class Deck:
    # This class makes a full deck of cards
    def __init__(self):
        self.cards = []

        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
                 "Jack", "Queen", "King", "Ace"]

        # Add all 52 cards to the deck
        for suit in suits:
            for rank in ranks:
                card = Card(rank, suit)
                self.cards.append(card)

    def shuffle(self):
        # Shuffle the cards
        random.shuffle(self.cards)

    def deal(self):
        # Deal one card from the deck
        return self.cards.pop()


def show_hand(hand):
    # Show the cards in the player's hand
    print("\nYour hand:")
    for i in range(5):
        print(i + 1, "-", hand[i])


def get_choices():
    # Ask the user which cards they want to replace
    choice = input("\nEnter card numbers to replace like 1,3,5 or press Enter to keep all: ")

    if choice == "":
        return []

    numbers = choice.split(",")
    replace_list = []

    for num in numbers:
        num = num.strip()
        if num.isdigit():
            num = int(num)
            if num >= 1 and num <= 5:
                if num not in replace_list:
                    replace_list.append(num)

    return replace_list


def replace_cards(hand, deck, replace_list):
    # Replace the chosen cards with new ones
    for num in replace_list:
        hand[num - 1] = deck.deal()


def main():
    # Create and shuffle the deck
    deck = Deck()
    deck.shuffle()

    # Deal 5 cards
    hand = []
    for i in range(5):
        hand.append(deck.deal())

    # Show first hand
    print("First Poker Hand")
    show_hand(hand)

    # Get cards to replace
    replace_list = get_choices()

    # Replace selected cards
    replace_cards(hand, deck, replace_list)

    # Show final hand
    print("\nFinal Poker Hand")
    show_hand(hand)

main()