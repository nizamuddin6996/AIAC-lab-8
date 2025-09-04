def is_sentence_palindrome(sentence):
    """
    Returns True if the given sentence is a palindrome,
    ignoring case, spaces, and punctuation.
    """
    cleaned = ''.join(
        c.lower() for c in sentence if c.isalnum()
    )
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    if is_sentence_palindrome(sentence):
        print("True")
    else:
        print("False")


