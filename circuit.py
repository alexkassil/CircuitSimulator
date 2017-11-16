from reader import *

def update(tokens, old, new):
    return [new if x == old else x for x in tokens]

class Circuit:
    inputs = None
    circuit = None
    def __init__(self, inputs, circuit):
        self.inputs = inputs
        self.circuit = circuit

    def test(self):
        circuit = self.circuit
        for inpt in self.inputs:
            circuit = update(circuit, inpt, 'True')
        circuit = update(circuit, '+', 'or')
        circuit = update(circuit, '*', 'and')
        circuit = update(circuit, '!', 'not')

        print(' '.join(circuit), eval(' '.join(circuit)))



