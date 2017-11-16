import string

from buffer import Buffer
from circuit import *

SYMBOL = set(string.ascii_lowercase + string.ascii_uppercase + string.digits + '_')
BASIC_CIRCUIT = set('+*!')
WHITESPACE = set(' \t\n\r')
DELIMITERS = set('()')

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
                    
