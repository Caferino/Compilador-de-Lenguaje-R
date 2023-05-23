"""
    Proyecto Final
    Autor: Óscar Antonio Hinojosa Salum A00821930
    Abril 15 2023
    Compilador para lenguaje al estilo R.
"""

# ============ Métodos globales ============

def validateSize(self, address):
    # Si la memoria son bytes negativos o más de lo que se asignó, que quiebre
    if address < 0 or address >= len(self.memory):
        raise Exception("Memory Overflow")
    
    # Si no, todo está bien, regresar TRUE
    return True



# ============ Main - Clase de Memoria ============

class MemoryMap:
    def __init__(self):
        # self.memory = [None] * size
        self.operands = []
        self.operators = []
        self.types = []
        self.memoryMap = {}

        # Symbol Table
        self.symbolTable = {}
        self.new_row = {}
        self.rowCount = 1
    

    def read(self, address):
        # Verificar que tenga un tamaño válido
        if(validateSize(address)):
            # Si es válido, regresar el valor en la dirección
            return self.memory[address]


    def write(self, address, value):
        # Verificar que tenga un tamaño válido
        if(validateSize(address)):
            # Si es válido, escribir el valor en la dirección
            self.memory[address] = value


    def p_varsEnter(self, vars_type, vars_name, var_size, var_dimensions, vars_assignment):
        self.types.append(vars_type)
        self.varsDir.append(vars_name)


    def insertRow(self, new_row):
        # Si la Symbol Table está vacía, insertar row sí o sí
        if not self.symbolTable:
            self.symbolTable[self.rowCount] = new_row
            self.rowCount = self.rowCount + 1

        # Si la Symbol Table NO está vacía, verificar existencia
        else:
            found = False
            for existing_row in self.symbolTable.values():
                print("Row: ")
                print(existing_row)
                if new_row == existing_row:
                    # ACTUALIZAR VALUE SOLAMENTE
                    found = True

            if not found:
                self.symbolTable[self.rowCount] = new_row
                self.rowCount = self.rowCount + 1

                
