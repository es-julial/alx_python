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

        Example:
            >>> bg = BaseGeometry()
            >>> bg.integer_validator("width", 10)  # Valid
            >>> bg.integer_validator("height", 12)  # Valid
            >>> bg.integer_validator("age", 0)  # Raises ValueError
            >>> bg.integer_validator("age", -4)  # Raises ValueError
            >>> bg.integer_validator("age", 13.5)  # Raises TypeError
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

# Test cases
bg = BaseGeometry()

# Output: List of attributes and methods of the object
print(dir(bg))

# Output: No exception is raised
bg.integer_validator("myint", 12)

# Output: No exception is raised
bg.integer_validator("width", 89)

# Output: Raises TypeError: "name" must be an integer
bg.integer_validator("name", "John")

# Output: Raises ValueError: "age" must be greater than 0
bg.integer_validator("age", 0)

# Output: Raises ValueError: "age" must be greater than 0
bg.integer_validator("age", -4)

# Output: Raises TypeError: "age" must be an integer
bg.integer_validator("age", 13.5)

# Output: Raises Exception: area() is not implemented
bg.area()
