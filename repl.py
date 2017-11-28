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
    global circuits
    while True:
        try:
            user_input = input('--> ')
            if user_input[0] != '.':
                circuit = tokenize(user_input)
                inputs = find_inputs(circuit)
                test = Circuit(inputs, circuit)
                print(inputs, circuit, test)
                test.logic_gate()
            else:
                command = user_input[1:]
                if command == 'unlock':
                    circuits.update(master_circuits)
                elif command == 'add':
                    print('circuit command: ')
                    circuit_command = input()
                    print('circuit description')
                    circuit_description = input()
                    print('circuit code')
                    circuit_code = input()
                    print(circuit_command, circuit_description, circuit_code)
                    circuits[circuit_command] = circuit_description
                    circuit = tokenize(circuit_code)
                    inputs = find_inputs(circuit)
                    
                    exec('global ' + circuit_command)
                    exec(circuit_command + ' = Circuit(inputs, circuit)')
                    test = Circuit(inputs, circuit)
                    test.logic_gate(True, circuit_command)
                    print(circuit, inputs, c)

                elif command in circuits:
                    print(circuits[command])
                else:
                    print('Unkown command:', command)
                
        except (SyntaxError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):
            print()
#            bye()
            break

