import string

from buffer import Buffer
from helpers import *

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

def is_input(token):
    for char in token:
        if char not in SYMBOL:
            return False
    return True
    
def find_inputs(tokens):
    inputs = []
    for token in tokens:
        if is_input(token):
            inputs.append(token)
    return inputs

def mass_circuit(tokens, pairs):
    for old, new, num_inputs in pairs:
        tokens = circuit_update(tokens, old, new, num_inputs)
    return tokens

def circuit_update(tokens, old, new, num_inputs):
    while old in tokens:
        for i in range(len(tokens)):
            if tokens[i] == old:
                d = replace(tokens, i, num_inputs)
                change = new.format(d=d)
                print(change)
                for j in range(len(tokens)):
                    if tokens[j] == old:
                        tokens[j] = change
                        break
                break
        print('!!!', tokenize(' '.join(tokens)))
    print(tokens, d)


    
def replace(tokens, i, num_inputs):
    result = []
    while num_inputs:
        result += [find_right(tokens, i)]
        print(result)
        num_inputs -= 1
        if num_inputs:
            result += [find_left(tokens, i)]
            print(result)
            i -= len(result)
            num_inputs -= 1
    return result

def find_right(tokens, i):
    current = tokens.pop(i+1)
    if current != '(':
        raise ValueError('Ill formated input (add parentheses!)')
    value = -1;
    while value:
        current += tokens.pop(i+1)
        if current[-1] == ')':
            value += 1
        if current[-1] == '(':
            value -= 1
    return current
    
def find_left(tokens, i):
    current = tokens.pop(i-1)
    i -= 1
    if current != ')':
        raise ValueError('Ill formated input (add parentheses!)')
    value = 1;
    while value:
        current += tokens.pop(i-1)
        i -= 1
        if current[-1] == ')':
            value += 1
        if current[-1] == '(':
            value -= 1
    return current[::-1]



