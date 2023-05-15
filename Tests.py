# Memoria virtual / Mapa de memoria

class MemoryMap:
    def __init__(self, size):
        # EVITAR HASHMAPS
        # RECORDAR LOS 4 SEGMENTOS (Data Segment, Code Segment, Stack Segment, Extra Segment)
        # IMPORTANTE: NO USAR UN TAMAÑO IGUAL PARA TODOS LOS SEGMENTOS, 
        # QUE SEA DINÁMICO, TIPO UN VECTOR QUE SE ALARGA CUANDO LO NECESITA
        self.memory = [None] * size
    
    def read(self, address):
        # Si la memoria son bytes negativos o más de lo que se tiene, que quiebre
        if address < 0 or address >= len(self.memory):
            raise Exception('ERROR')
        return self.memory[address]
    
    def write(self, address, value):
        # Meter valor en direccion
        self.memory[address] = value


# Virtual Machine

class VirtualMachine:
    def __init__(self):
        self.stack = []
        self.program_counter = 0

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) == 0:
            raise RuntimeError('Empty stack')
        return self.stack.pop()

# Las operaciones tipo CPU serán un switchesote, algo así:

"""
elif op == 'ADD':
    b = self.pop()
    a = self.pop()
    self.push(a + b)

elif op == 'SUB':
    b = self.pop()
    a = self.pop()
    self.push(a - b)

elif op == 'MUL':
    b = self.pop()
    a = self.pop()
    self.push(a * b)

elif op == 'DIV':
    b = self.pop()
    a = self.pop()
    self.push(a / b)

    ...
"""

# Usar un stack

# Operaciones aritméticas, como si fuese el CPU

# Trabaja en conjunto con la Memoria, lo que aún no sé es cómo intervienen en el Parser o Léxico?

"""
¿Así?
def p_extra_vars(p):
    '''extra_vars : COMMA ID interventionFunctionOrNeuronalNode() vars_equals
                | empty'''

interventionFunctionOrNeuronalNode() // Would go above, I know
    Stuff stuff with memory
    Access address, verify types, write or save variables in a dynamic data structure

"""


# Matriz de Type Matchmaking

typeMatch = ['LEFTOPTYPE', 'RIGHTOPTYPE', '^', '*', '/', '%',
             '+', '-', '>', '<', '<>', '!=', '==', '=', '&&', '||'
             ]['INT', 'INT', 'INT', 'INT', 'FLOAT', 'FLOAT', 'FLOAT', 'FLOAT', 'CHAR',
             'CHAR', 'CHAR', 'CHAR', 'BOOL', 'BOOL', 'BOOL', 'BOOL']



# Matriz de Direcciones

varDirs = ['NAME', 'TYPE', 'SCOPE', 'FUNCTION', 'VARS']['1', '2', '3']



# Nodos neuronales

