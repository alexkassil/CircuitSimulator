from reader import *

def update(tokens, old, new):
    return [new if x == old else x for x in tokens]

def mass_update(tokens, pairs):
    for old, new in pairs:
        tokens = update(tokens, old, new)
    return tokens

class Circuit:
    inputs = None
    circuit = None
    def __init__(self, inputs, circuit):
        self.inputs = inputs
        self.circuit = mass_update(circuit, [['+', 'or'], ['*', 'and'], ['!', 'not']])

    def logic_gate(self):
        for inpt in self.inputs:
            print(inpt, ' | ', end="")
        print('out ', end='')
        print()
        num = len(self.inputs)
        for i in range(num**2):
            pairs = []
            circuit = self.circuit
            for j in range(num):
                print(i%2, end=" ")
                print(' | ', end="")
                pairs.append([self.inputs[j], str(i%2 == 1)])
                i = i // 2
            circuit = mass_update(circuit, pairs)
            print(1 if eval(' '.join(circuit)) else 0)
        
    def test(self):
        circuit = self.circuit

        for inpt in self.inputs:
            circuit = update(circuit, inpt, 'True')

        print(' '.join(circuit), eval(' '.join(circuit)))



