class BaseGeometry:
    """Base class for geometry.

    This class provides a base for other geometry classes to inherit from.

    Methods:
        area(self): Raises an Exception with the message "area() is not implemented".
        integer_validator(self, name, value): Validates the integer value.

    Attributes:
        name: The name of the value being validated.
        value: The integer value to be validated.
    """

    def area(self):
        """Calculate the area of the geometry.

        Raises:
            Exception: Always raises an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the integer value.

        Args:
            name (str): The name of the value being validated.
            value: The integer value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """A class representing a rectangle.

    This class inherits from BaseGeometry and adds functionality specific to rectangles.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height


# Test cases
rectangle = Rectangle(5, 10)
print(rectangle.__dict__)  # Output: {'_BaseGeometry__width': 5, '_BaseGeometry__height': 10}
