from reader import *
from helpers import *

class Circuit:
    inputs = None
    circuit = None
    def __init__(self, inputs, circuit):
        self.inputs = remove_duplicates(inputs)
        self.circuit = mass_circuit_update(circuit, [['+', 'not ({d[1]} and {d[0]})', 2]])
#        self.circuit = mass_update(circuit, [['+', 'or'], ['*', 'and'], ['!', 'not']])

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



