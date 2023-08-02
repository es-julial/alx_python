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

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """Generate the string representation of the rectangle.

        Returns:
            str: The formatted string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """A class representing a square.

    This class inherits from Rectangle and adds functionality specific to squares.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2


# Test cases
print(dir(Square))  # Output: List of attributes and methods of the Square class

print(issubclass(Square, Rectangle))  # Output: True (Square is a subclass of Rectangle)

s = Square(4)
print(s.area())  # Output: 16

s = Square(1340)
print(s.area())  # Output: 1795600

s = Square()
# Output: TypeError: __init__() missing 1 required positional argument: 'size'

s = Square("13")
# Output: TypeError: size must be an integer

s = Square(13)
print(s.width)  # Output: 13
print(s.height)  # Output: 13
