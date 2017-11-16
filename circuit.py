from reader import *

class Circuit:
    inputs = None
    circuit = None
    def __init__(self, inputs, circuit):
        self.inputs = inputs
        self.circuit = circuit

    def test(self):
        circuit = self.circuit
        for inpt in inputs:
            circuit = ['True' if inpt == x else x for x in circuit]
        print(' '.join(circuit), eval(circuit))
