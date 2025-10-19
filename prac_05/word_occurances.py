"""
Word Occurrences
Estimate: 15 minutes
Actual:   (record your actual time here)
"""

def main():
    """Count how many times each word appears in a given text."""
    text = input("Text: ").lower()
    words = text.split()

    word_counts = {}
    for word in words:
        # If word already in dictionary, increment; else start at 1
        word_counts[word] = word_counts.get(word, 0) + 1

    # Sort words alphabetically
    sorted_words = sorted(word_counts.keys())

    # Find the longest word for alignment
    max_length = max(len(word) for word in sorted_words)

    # Display results neatly aligned
    for word in sorted_words:
        print(f"{word:{max_length}} : {word_counts[word]}")


main()
