try:
    import readline
except ImportError:
    pass

from bye import *
from reader import *
from circuit import *



# repl start
if __name__ == '__main__':
    circuit = None
    while True:
        try:
            user_input = input('--> ')
            if user_input[0] != '.':
                circuit = tokenize(user_input)
                inputs = find_inputs(circuit)
                test = Circuit(inputs, circuit)
                test.logic_gate()
            else:
                command = user_input[1:]
                if command in circuits:
                    print(circuits[command])
                else:
                    print('Unkown command:', command)
                
        except (SyntaxError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):
            print()
#            bye()
            break

