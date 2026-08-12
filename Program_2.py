import string


def analyze_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Remove extra whitespace and split into words
    words = text.split()

    # Total word count
    total_words = len(words)

    # Frequency table
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    # Find palindromes
    palindromes = []

    for word in frequency:
        if len(word) > 1 and word == word[::-1]:
            palindromes.append(word)

    # Display report
    print("\nText Analysis Report")
    print("Total words:", total_words)

    print("\nWord Frequency:")
    for word, count in sorted(frequency.items()):
        print(word, ":", count)

    print("\nPalindromes:")
    if palindromes:
        print(", ".join(sorted(palindromes)))
    else:
        print("No palindromes found.")


# Multiline string input
text = """
Madam went to the market.
Madam travelled for 30 minutes.
The market was busy.
Madam brought apples.
"""

analyze_text(text)