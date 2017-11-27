from reader import *

class Circuit:
    def __init__(self, inputs, circuit):
        self.inputs = remove_duplicates(inputs)
        self.circuit = circuit
        
    def __initOLD__(self, inputs, circuit):
        self.inputs = remove_duplicates(inputs)
        self.circuit = mass_update(circuit, [['+', 'or'], ['*', 'and'], ['!', 'not']])

    def logic_gate(self):
        longest = max(len(self.inputs[0]), 3)
        display_first(self.inputs, longest)
        print(('-' * (longest + 3)) * (len(self.inputs)+1))
        display_rest(self.inputs, self, longest)

    def eval(self, args):
        if len(args) != len(self.inputs):
            raise ValueError("Mismatched Number of Inputs")
        with_inputs = ' '.join(mass_update(self.circuit, zip(self.inputs, args)))
        print(with_inputs)
        return eval(with_inputs)
        
    def test(self):
        circuit = self.circuit

        for inpt in self.inputs:
            circuit = update(circuit, inpt, 'True')

        print(' '.join(circuit), eval(' '.join(circuit)))

circuits = {
    'c_and' : Circuit(['a', 'b'], 'a and b'),
    'c_not' : Circuit(['a'], 'not a')
    }

def c_and(x, y):
    return x and y

#def c_not(x):
#    return not x

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

def display_first(inputs, longest):
    for inpt in inputs:
        print(inpt, end='')
        print(' ' * (longest - len(inpt) + 1), end='')
        print('| ', end='')
    print('out')

def display_rest(inputs, circuit, longest):
    n = len(inputs)
    for binary_digit in range(pow(2, n)):
        values = to_true_false(binary_digit, n)
        display_row(values, circuit.eval(values), longest)

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
