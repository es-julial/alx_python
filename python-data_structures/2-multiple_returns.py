
def multiple_returns(sentence):
    # Check if the sentence is empty
    if not sentence:
        # If the sentence is empty, return None for the first character
        return (0, None)

    # Get the length of the sentence using len()
    length = len(sentence)

    # Return a tuple containing the length and the first character
    return (length, sentence[0])
