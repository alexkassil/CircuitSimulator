from circuit import *

circuits = {
    'c_nand' : 'NAND GATE : 2 Inputs',
    'c_not'  : 'NOT GATE : 1 Input',
    'c_and'  : 'AND GATE : 2 Inputs',
    'c_or'   : 'OR GATE : 2 Inputs',
    'c_xor'  : 'XOR GATE : 2 Inputs'
}

c_nand = Circuit(['a', 'b'], ['not', '(', 'a', 'and', 'b', ')'])
c_not = Circuit(['a'], ['c_nand', '(', 'a', ',', 'b', ')'])
