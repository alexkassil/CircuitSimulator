try:
    import readline
except ImportError:
    pass

from bye import *
from reader import *

class Circuit:
    def __init__(self, inputs, circuit):
        self.inputs = remove_duplicates(inputs)
        self.circuit = circuit
        
    def logic_gate(self, secret=False, name=None):
        if not secret:
            longest = max(len(self.inputs[0]), 3)
            display_first(self.inputs, longest)
            print(('-' * (longest + 3)) * (len(self.inputs)+1))
            display_rest(self.inputs, self, longest)

    def eval(self, args):
        if len(args) != len(self.inputs):
            raise ValueError("Mismatched Number of Inputs")
        with_inputs = ' '.join(mass_update(self.circuit, zip(self.inputs, args)))
        return eval(with_inputs)

    def __call__(self, *args):
        return self.eval([str(arg) for arg in args])
    
c_nand = Circuit(['a', 'b'], ['not', '(', 'a', 'and', 'b', ')'])
c_not = Circuit(['a'], tokenize('c_nand(a, a)'))
c_and = Circuit(['a', 'b'], tokenize('c_not(c_nand(a, b))'))
    
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


# repl start
if __name__ == '__main__':
    circuit = None
    global circuits
    while True:
        try:
            user_input = input('--> ')
            if user_input[0] != '.':
                circuit = tokenize(user_input)
                inputs = find_inputs(circuit)
                test = Circuit(inputs, circuit)
                print(inputs, circuit, test)
                test.logic_gate()
            else:
                command = user_input[1:]
                if command == 'unlock':
                    circuits.update(master_circuits)
                elif command == 'add':
                    print('circuit command: ')
                    circuit_command = input()
                    print('circuit description')
                    circuit_description = input()
                    print('circuit code')
                    circuit_code = input()
                    circuits[circuit_command] = circuit_description
                    circuit = tokenize(circuit_code)
                    inputs = find_inputs(circuit)
                    exec('global ' + circuit_command)
                    exec(circuit_command + ' = Circuit(inputs, circuit)')

                elif command in circuits:
                    print(circuits[command])
                else:
                    print('Unkown command:', command)
                
        except (SyntaxError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):
            print()
#            bye()
            break
