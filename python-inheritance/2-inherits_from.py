"""
This module checks if an instance is directly
or indirectly a n instance of specific class
"""
def inherits_from(obj, a_class):
    """
    check if obj is an instance of class
    Args:
        obj ([type]): object
        a_class ([type]): a class
    Returns:
        True: obj is an instance of a_class
        False: obj not an instance of a_class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False