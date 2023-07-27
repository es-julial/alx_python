def best_score(a_dictionary):
    if not a_dictionary:
        return None

    # Initialize variables to keep track of the best score and the corresponding key
    best_key = None
    best_score = float('-inf')  # Negative infinity, to handle negative scores if present

    # Iterate through the dictionary items
    for key, value in a_dictionary.items():
        if value > best_score:
            best_key = key
            best_score = value

    return best_key
