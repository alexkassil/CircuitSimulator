try:
    import readline
except ImportError:
    pass

from bye import *
from reader import *
from circuit import *

# repl start
if __name__ == '__main__':
    while True:
        try:
            user_input = input('--> ')
            circuit = tokenize(user_input)
            inputs = find_inputs(circuit)
            test = Circuit(inputs, circuit)
            test.logic_gate()
        except (SyntaxError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):
            print()
#            bye()
            break
        
