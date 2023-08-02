"""
This module checks if an object is instance of a class or a subclass
"""
def is_kind_of_class(obj, a_class):
    """AI is creating summary for is_kind_of_class

    Args:
        obj: the instance/object
        a_class: a class

    Returns:
        True: if bj is instance of the class
        False: if obj not object of the class 
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False