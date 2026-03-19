import re

def split_into_sentences(paragraph):
    # This function uses look-behind and look-ahead to split a paragraph
    # into individual sentences.
    # It splits after ., ?, or ! followed by whitespace,
    # when the next sentence starts with a capital letter, a number, or a quote.

    pattern = r'(?<=[.!?])\s+(?=[A-Z0-9"])'

    # Split the paragraph into a list of sentences
    sentences = re.split(pattern, paragraph)

    return sentences


def display_sentences(sentences):
    # This function displays each sentence and the total sentence count.

    print("\nIndividual Sentences:")

    for index, sentence in enumerate(sentences, start=1):
        print(f"{index}. {sentence}")

    print(f"\nTotal number of sentences: {len(sentences)}")

def main():
    # This function gets the paragraph from the user,
    # calls the sentence-splitting function,
    # and displays the results.

    paragraph = input("Enter a paragraph: ")

    sentences = split_into_sentences(paragraph)

    display_sentences(sentences)


main()