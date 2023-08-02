# my_module.py

class BaseGeometry:
    """Base class for geometry.

    This class provides a base for other geometry classes to inherit from.

    Methods:
        area(self): Raises an Exception with the message "area() is not implemented".
    """

    def area(self):
        """Calculate the area of the geometry.

        Raises:
            Exception: Always raises an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")
