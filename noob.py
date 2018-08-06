def mod(a, b):
    if b == 0:
        raise ZeroDivisionError
    
    remainder = a
    while remainder >= b:
        remainder -= b
    
    return remainder
    