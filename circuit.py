from reader import *

def update(tokens, old, new):
    return [new if x == old else x for x in tokens]

def mass_update(tokens, pairs):
    for old, new in pairs:
        tokens = update(tokens, old, new)
    return tokens

def to_true_false(digit, n):
    """ Turn digit into n True/False values
    based on each bit in digit.
    >>> to_true_false(3, 4)
    [False, False, True, True]
    """
    result = []
    while n:
        current = pow(2, n-1)
        if ((digit - current) >= 0):
            result.append('True')
            digit -= current
        else:
            result.append('False')
        n -= 1
    return result

def display_first(inputs, circuit, longest):
    for inpt in inputs:
        print(inpt, end='')
        print(' ' * (longest - len(inpt) + 1), end='')
        print('| ', end='')
    print('out')

def display_rest(inputs, circuit, longest):
    n = len(inputs)
    for binary_digit in range(pow(2, n)):
        values = to_true_false(binary_digit, n)
        output = mass_update(circuit, zip(inputs, values))
        display_row(values, eval(' '.join(output)), longest)

def display_row(values, output, longest):
    for value in values:
        print(1 if eval(value) else 0, end='')
        print(' ' * (longest-1), '| ', end='')
    print(1 if output else 0)
        
def remove_duplicates(inputs):
    result = [inputs[0]]
    for inpt in inputs:
        if inpt not in result:
            result.append(inpt)
    return result

class Circuit:
    inputs = None
    circuit = None
    def __init__(self, inputs, circuit):
        self.inputs = remove_duplicates(inputs)
        self.circuit = mass_update(circuit, [['+', 'or'], ['*', 'and'], ['!', 'not']])

    def logic_gate(self):
        longest = max(len(self.inputs[0]), 3)
        display_first(self.inputs, self.circuit, longest)
        print(('-' * (longest + 3)) * (len(self.inputs)+1))
        display_rest(self.inputs, self.circuit, longest)
        
        
    def test(self):
        circuit = self.circuit

        for inpt in self.inputs:
            circuit = update(circuit, inpt, 'True')

        print(' '.join(circuit), eval(' '.join(circuit)))



