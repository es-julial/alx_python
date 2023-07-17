def validate_password(password):
    if len(password) < 8:
        return False
    digit = False
    lower = False
    upper = False

    for char in password:
        if char.islower():
            lower = True
        elif char.isupper():
            upper = True
        elif char.isdigit():
            digit = True
        elif char == ' ':
            return False
    if digit and lower and upper:
        return True
    else:
        return False
