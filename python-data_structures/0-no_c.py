

# File: 0-no_c.py

def no_c(my_string):
    result = []
    for char in my_string:
        if char not in ['c', 'C']:
            result.append(char)
    return ''.join(result)
