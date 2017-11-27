import string

from buffer import Buffer
from helpers import *

SYMBOL = set(string.ascii_lowercase + string.ascii_uppercase + string.digits + '_')
BASIC_CIRCUIT = set('+*!')
WHITESPACE = set(' \t\n\r')
DELIMITERS = set('(,)')

circuits = ['c_and', 'c_not']

def tokenize(s):
    src = Buffer(s)
    tokens = []
    while True:
        token = next_token(src)
        if token is None:
            return tokens
        tokens.append(token)

def take(src, allowed_characters):
    result = ''
    while src.current() in allowed_characters:
        result += src.remove_front()
    return result

def next_token(src):
    take(src, WHITESPACE)
    c = src.current()
    if c is None:
        return None
    elif c in SYMBOL:
        return take(src, SYMBOL)
    elif c in DELIMITERS:
        src.remove_front()
        return c
    elif c in BASIC_CIRCUIT:
        return src.remove_front()
    else:
        raise SyntaxError("'{}' is not a token".format(c))

def is_input(token):
    for char in token:
        if char not in SYMBOL:
            return False
    return True
    
def find_inputs(tokens):
    inputs = []
    for token in tokens:
        if is_input(token) and token not in circuits:
            inputs.append(token)
    return inputs

