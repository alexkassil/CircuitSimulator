from reader import *
from circuit import *

user_input = tokenize('A+B+C')
circuit = tokenize(user_input)
inputs = find_inputs(circuit)
test = Circuit(inputs, circuit)
