# This program asks the user to enter an email message.
# It scans the message for 30 common spam words/phrases.
# Each time a spam word appears, 1 point is added to the spam score.
# The program then displays:
#   1. Total spam score
#   2. Likelihood the message is spam
#   3. Which words were found

# ----------------------------------------------------------
# Function 1:
# This function returns a list of 30 spam words/phrases
# ----------------------------------------------------------
def get_spam_words():
    return [
        "free", "buy now", "winner", "prize", "coupon",
        "discount", "clearance", "special offer", "limited time offer",
        "exclusive deal", "act now", "urgent", "today only",
        "last chance", "don't miss out", "offer expires",
        "while stocks last", "hurry", "instant access", "save big",
        "risk-free", "no obligation", "deal", "best price",
        "serious bargain", "bonus", "cheap", "earn extra cash",
        "get paid", "work from home"]

