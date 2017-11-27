circuits = ['c_and', 'c_not', 'c_nand']

def c_nand(a, b):
    return not (a and b)

def c_not(a):
    return c_nand(a, a)

def c_and(a, b):
    return c_not(c_nand(a, b))
