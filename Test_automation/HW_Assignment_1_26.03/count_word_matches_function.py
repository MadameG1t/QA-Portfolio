def count_word_matches(text, target):
    """
    Counts the number of times a target word appears as a standalone word in the text.
    Matching is case-insensitive, and words are separated by spaces.

    Args:
        text (str): The input string to search in.
        target (str): The word to search for.

    Returns:
        int: Number of times the target word appears as a standalone word.
    """
    if not text or not target:
        return 0

    # Split text into words and convert to lowercase for case-insensitive matching
    words = text.lower().split()
    target = target.lower()

    # Count standalone occurrences of the target word
    return words.count(target)