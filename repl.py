try:
    import readline
except ImportError:
    pass

from bye import *
from reader import *

class Circuit:
    def __init__(self, inputs, circuit):
        self.inputs = inputs
        self.circuit = circuit
        
    def logic_gate(self, secret=False, name=None):
        if not secret:
            longest = max(longest_input(self.inputs), 3)
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
    
c_nand = Circuit(['a', 'b'], tokenize('not(a and b)'))
c_not = Circuit(['a'], tokenize('c_nand(a, a)'))
c_and = Circuit(['a', 'b'], tokenize('c_not(c_nand(a, b))'))
c_or = Circuit(['a', 'b'], tokenize('c_nand(c_nand(a, a), c_nand(b, b))'))
c_xor = Circuit(['a', 'b'], tokenize('c_and(c_or(a, b), c_nand(a, b))'))
c_nor = Circuit(['a', 'b'], tokenize('c_not(c_or(a, b))'))
c_and_8_code = 'c_and(c_and(c_and(a, b), c_and(c, d)), c_and(c_and(e, f), c_and(g, h)))'
c_and_8 = Circuit(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], tokenize(c_and_8_code))

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

def longest_input(lst):
    return len(max(lst, key=len))

# repl start
if __name__ == '__main__':
    circuit = None
    global circuits
    print("Type .help for assistance!")
    while True:
        try:
            user_input = input('--> ')
            if user_input[0] != '.':
                try:
                    circuit = tokenize(user_input)
                    inputs = find_inputs(circuit)
                    test = Circuit(inputs, circuit)
                    test.logic_gate()
                except RuntimeError:
                    print("Input", user_input, "is not well formated!!!")
            else:
                command = user_input[1:]
                if command == 'unlock':
                    circuits.update(master_circuits)
                elif command == 'help':
                    print('Avaliable commands:\n.circuits\n.add\n.unlock\n\nSimulate circuit with "circuit_name(var1, var2, ...)"\nExample: c_nand(a, b)')
                elif command == 'circuits':
                    print('Type ."circuit_name" for more info about each circuit!')
                    for circuit in circuits:
                        print(circuit)
                elif command == 'add':
                    print('circuit command: ')
                    circuit_command = input()
                    while (circuit_command == 'not' or circuit_command == 'and'):
                        print('"not" and "and" are not allowed to be your circui_name!\nNew name:')
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
            bye()
            break
