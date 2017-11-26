from reader import *
from circuit import *
from helpers import *

user_input = tokenize('(((A)+(B))+(C))')
circuit = tokenize(user_input)
inputs = find_inputs(circuit)
test = Circuit(inputs, circuit)
