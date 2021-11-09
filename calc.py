def add(x, y):
    """Add function"""
    return x + y


def substract(x, y):
    """"Suvstract function"""
    pass


def multiply(x, y):
    """Multiply function"""
    return x * y


def divide(x, y):
    """Divide function"""
    if y == 0:
        raise ValueError('Can not divide by zero')
    return x / y
