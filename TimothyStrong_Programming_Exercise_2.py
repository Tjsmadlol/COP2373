# This program asks the user to enter an email message.
# It scans the message for 30 common spam words/phrases.
# Each time a spam word appears, 1 point is added to the spam score.
# The program then displays:
#   1. Total spam score
#   2. Likelihood the message is spam
#   3. Which words were found

# Function 1: returns the list of spam words/phrases
# ----------------------------------------------------------
def get_spam_words():
    spam_words = ["free","free money","act now","urgent","limited time","don't miss out","hurry","winner",
        "congratulations","prize","cash bonus","earn extra cash","make money","get paid","fast cash","financial freedom",
        "work from home","be your own boss","additional income","no obligation","risk free","best price","exclusive deal",
        "special offer","buy now","instant access","click here","limited offer","final notice","guaranteed"]
    return spam_words

# Function 2:
# This function checks the email for spam words
# It returns:
#   - spam score (number of times words appear)
#   - list of words that were found
def check_spam(message, spam_words):

    # Convert message to lowercase so matching is easier
    message = message.lower()

    # Start spam score at 0
    score = 0

    # List to store words that were found
    found_words = []

    # Go through each spam word
    for word in spam_words:

        # Count how many times that word appears
        count = message.count(word)

        # Add that number to the score
        score = score + count

        # If the word was found at least once, save it
        if count > 0:
            found_words.append(word)

    # Send results back to main program
    return score, found_words
# Function 3:
# This function decides how likely the email is spam
# based on the spam score
def get_rating(score):

    if score == 0:
        return "Not likely spam"
    elif score <= 3:
        return "Low chance of spam"
    elif score <= 7:
        return "Moderate chance of spam"
    elif score <= 12:
        return "High chance of spam"
    else:
        return "Very high chance of spam"
# MAIN PROGRAM
if __name__ == "__main__":

    spam_words = get_spam_words()

    print("Enter an email message:")
    email_message = input()

    score, found_words = check_spam(email_message, spam_words)
    rating = get_rating(score)

    print("\nSpam Score:", score)
    print("Spam Likelihood:", rating)

    print("Spam words found:")
    if len(found_words) == 0:
        print("None")
    else:
        for word in found_words:
            print("-", word)