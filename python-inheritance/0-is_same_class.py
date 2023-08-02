def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Parameters:
        obj: Any - The object to check.
        a_class: type - The class to compare against.

    Returns:
        bool: True if the object is an instance of the specified class; otherwise, False.
    """
    return type(obj) == a_class


# Test cases
a = 1
print(is_same_class(a, int))  # Correct output: True

a = True
print(is_same_class(a, int))  # Correct output: False

a = 3.14
print(is_same_class(a, int))  # Correct output: False

a = True
print(is_same_class(a, object))  # Correct output: False

a = None
print(is_same_class(a, object))  # Correct output: True

a = None
print(is_same_class(a, list))  # Correct output: False

a = [1, 2, 3]
print(is_same_class(a, list))  # Correct output: True

a = [1, 2, 3]
print(is_same_class(a, object))  # Correct output: False
