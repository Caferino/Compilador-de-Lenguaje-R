"""
    Proyecto Final
    Autor: Óscar Antonio Hinojosa Salum A00821930
    Abril 15 2023
    Compilador para lenguaje al estilo R.

    Reglas de Semántica
"""

# ======================== Semántica ======================== #

import re # Librería para expresiones regulares RegEX
import pprint # Para imprimir el Symbol Table de manera bonita

from Quadruples import quadsConstructor

from Memory import MemoryMap
memory = MemoryMap()

typeMatchTable = [
    #    OpI   OpD   ^    *    /    %    +    -    >    <   <>   !=   ==    =   &&   ||
    #    ------------------------------------------------------------------
    ['int', 'int', 'int', 'int', 'float', 'int', 'int', 'int', 'bool', 'bool', 'bool', 'bool', 'bool', 'int', 'bool', 'bool'],
    ['int', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'bool', 'bool', 'bool', 'bool', 'bool', 'float', 'bool', 'bool'],
    ['int', 'char', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'bool', 'bool', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],
    ['int', 'bool', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'bool', 'bool', 'bool', 'bool', 'bool', 'bool', 'bool', 'bool'],
    ['float', 'int', 'float', 'float', 'float', 'float', 'float', 'float', 'bool', 'bool', 'bool', 'bool', 'bool', 'float', 'bool', 'bool'],
    ['float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'bool', 'bool', 'bool', 'bool', 'bool', 'float', 'bool', 'bool'],
    ['float', 'char', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'bool', 'bool', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],
    ['float', 'bool', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'bool', 'bool', 'bool', 'bool', 'bool', 'bool', 'bool', 'bool'],
    ['char', 'int', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'bool', 'bool', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],
    ['char', 'float', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'bool', 'bool', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],
    ['char', 'char', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'bool', 'bool', 'char', 'ERROR', 'ERROR', 'ERROR'],
    ['char', 'bool', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'bool', 'bool', 'bool', 'bool', 'ERROR', 'ERROR'],
    ['bool', 'int', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'bool', 'bool', 'bool', 'bool', 'bool', 'bool', 'bool', 'bool'],
    ['bool', 'float', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'bool', 'bool', 'bool', 'bool', 'bool', 'bool', 'bool', 'bool'],
    ['bool', 'char', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'bool', 'bool', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],
    ['bool', 'bool', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'bool', 'bool', 'bool', 'bool', 'bool', 'bool']
]

class Rules:
    def __init__(self):
        self.type = ''
        self.varName = ''
        self.varDimensions = []
        self.scope = 'global'
        self.isFunction = False
        self.values = []
        self.varValues = []
        self.parentFunction = None

        # Auxiliares
        self.openList = False
        self.currentFunctionParams = []
        self.tuplesToModify = []
        self.allTypes = []
        self.inFunction = False
        self.opStack = []


    # ------ TYPES ------ #
    def p_insertType(self, p):
        self.type = p[1]
        self.allTypes.append(p[1])


    # ------ SCOPE ------ #
    def p_insertScope(self, scope):
        self.scope = scope


    # ------ FUNCTION PARAMETER ------ #
    # Esta función mete la variable parámetro en una pila para después
    # asociarlas con el nombre de la función, la cual llega al final
    def p_saveLocalVariable(self, p):
        if len(p) > 2 : self.currentFunctionParams.append(p[2])


    # ------ REGISTER FUNCTION PARAMETER ------ #
    # Esta función vaciará la pila con todas las variables locales de la
    # función a la vez que las registra como tal
    def p_registerLocalVariables(self, p):
        if len(p) > 2:
            functionName = p[2] ## functionParent
            # Empezamos el escaneo de la Symbol Table desde las variables
            # más recientes porque esas serán las de la función, así me guardo
            # procesamiento, creo que de lo mejor, O(1), creo. 
            stackLength = len(self.currentFunctionParams) - 1
            memoryLength = len(memory.symbolTable) - 1

            while stackLength > -1:
                # print("Objetos del symbol table: ", memory.symbolTable[memoryLength][5]) # ! DEBUG
                # Sacamos la fila del symbol table con una variable local por actualizar
                currentRow = memory.symbolTable[memoryLength]
                # Actualizamos la columna "functionParent"
                index_to_change = 5
                currentRow = currentRow[:index_to_change] + (functionName,) + currentRow[index_to_change + 1:]
                # Ponemos la nueva fila de vuelta
                memory.symbolTable[memoryLength] = currentRow

                # De una vez actualizo sus types también
                """ index_to_change = 0
                currentRow = (self.allTypes.pop(),) + currentRow[index_to_change + 1:]
                memory.symbolTable[memoryLength] = currentRow """
                
                
                memoryLength -= 1
                stackLength -= 1

            # Vaciamos la pila
            self.currentFunctionParams = []
            
            
            
            """ print("Function Name: ", functionName)
            print('Current parameters: ', self.currentFunctionParams) """





    # ------ VARIABLES / IDs ------ #
    def p_insertID(self, p, isFunction):
        # El ID siempre tendrá que ser el primer TOKEN de p, lo buscamos
        for row in p:
            # Condicional respetando estructura de "p_vars" y "p_extra_vars" en Parser.py
            if row != None and row != ',':
                varName = row  # Por legibilidad, en vez de 'self.varName'

                # Si tiene brackets pegados, es una matriz
                # Separamos el nombre de sus dimensiones
                if "[" in varName:
                    # Separamos el nombre de las dimensiones
                    varNameIndex = varName.index('[')
                    varName = varName[:varNameIndex]

                    # Guardamos las dimensiones
                    indices = re.findall(r'\[(.*?)\]', row)
                    indices = [int(index) for index in indices]
                    self.varDimensions = indices

                self.varName = varName

                # Si es una variable local, la anexamos con su función para facilitarme la vida después
                if self.scope == 'local' and varName not in self.currentFunctionParams: 
                    self.currentFunctionParams.append(varName)

                # Descubrí que para meter los values tendré que crear una pila que los separe por las comas
                # Ya que estoy leyendo esto de derecha a izquierda, arigato ozymndas
                
                # Separamos las variables en self.values con sus respectivas variables
                if self.values : topValue = self.values.pop()
                else : topValue = ','
                while topValue != ',' and topValue != '}':
                    # Si es un signo de menos, juntarlo con el siguiente valor
                    if topValue == '-' : topValue = float(self.varValues.pop()) * -1

                    self.varValues.append(topValue)
                    if self.values : topValue = self.values.pop()
                    else : break
                
                # Antes de meter los values, conviene transformar sus elementos al type apropiado
                if self.type == 'int':
                    self.varValues = [int(num) for num in self.varValues]
                # Como ya llegan como floats... ignoramos ese caso
                # Con bools puede ser, x > 0 = True, x == 0 or x == -1 = False tal vez, gusto propio...

                # Por leerse de derecha a izquierda, ocupamos girarlos...
                self.varValues.reverse()

                # print("Current Values: ", self.varValues) # ! DEBUG

                # Sacamos el type más actual, por si llegasen a ser parámetros
                # Al declarar multiples variables (e.g. int a, b, c ...) solo
                # se guarda un type a la vez, por ello esta pila allTypes
                if len(self.allTypes) > 0 : self.type = self.allTypes.pop()

                # Insertamos la data en forma de TUPLA a la Symbol Table
                memory.insertRow( (self.type, self.varName, self.varDimensions, self.scope, isFunction, self.parentFunction, self.varValues) )
                
                # Reseteamos auxiliares
                self.varValues = [] # Vaciamos los valores de esta variable para prestársela a la siguiente
                self.isFunction = False
                self.varDimensions = []
                self.parentFunction = None
                topValue = None

                # Al ya tener el ID/Valores, ignoramos lo que siga de la production rule
                break



    # ------ VALUES ------ #
    # Comas para separar los valores/listas de valores de cada variables
    def p_saveComma(self, p):
        self.values.append(p[1])


    # Si es un signo primero
    def p_saveSign(self, p):
        if p[1] == '-':
            self.values.append(p[1])


    # La super pila Operadores que guardará todos los tokens necesarios del programa
    # para las operaciones de los cuádruplos
    def p_saveToOpStack(self, p):
        if p[1] != None : self.opStack.append(p[1])
        else : self.opStack.append(';')


    # Si es un valor numérico o lista de
    def p_saveValue(self, p):
        # Si estamos en una lista, guardar cada elemento temporalmente
        if '{' not in str(p[1]) and '}' not in str(p[1]):
            self.values.append(p[1])

        # Si ya se va a cerrar la lista, cerramos este loop
        if len(p) > 2:
            if '}' in str(p[3]):
                self.values.append(p[3])
                
            elif '}' in str(p[4]): # Respecto a las production rules
                self.openList = False

        # Si no es valor de una lista/matriz, lo agregamos directamente
        if '{' in str(p[1]):
            self.openList = True  # Si el value viene dentro de "{}", será una lista de uno o más



    # ------ FUNCTION ------ #
    def p_function(p):
        '''
        1.- Insert Procedure self.name into the DirFunc table, verify semantics.

        2.- Insert every parameter into the current (local) VarTable.
        3.- Insert the type to every parameter uploaded into the VarTable. At the same time into the ParameterTable
        (to create the Function’s signature)..

        4.- Insert into DirFunc the number of parameters defined. **to calculate the workspace required for execution

        5.- Insert into DirFunc the number of local variables defined. **to calculate the workspace required for execution
        6.- Insert into DirFunc the current quadruple counter (CONT), **to establish where the procedure starts

        7.- Release the current VarTable (local).
        Generate an action to end the procedure (ENDFUNC).
        Insert into DirFunc the number of temporal vars used. **to calculate the workspace required for execution
        '''


    # ------ FUNCATION CALL ------ #
    def p_functionCall(p):
        '''
        1.- Verify that the procedure exists into the DirFunc.
        
        2.- Generate action ERA size (Activation Record expansion –NEW—size).
        Start the parameter counter (k) in 1.
        Add a pointer to the first parameter type in the ParameterTable.

        3.- Argument= PilaO.Pop() ArgumentType= PTypes.Pop().
        Verify ArgumentType against current Parameter (#k) in ParameterTable.
        Generate action PARAMETER, Argument, Argument#k

        4.- K = K + 1, move to next parameter.

        5.- Verify that the last parameter points to null (coherence in number of parameters).

        6.- Generate action GOSUB, procedure-self.name, , initial-address
        '''



    # ------ IF / ELSE ------ #
    def p_elif(p):
        '''
        1.- exp_type = PTypes.Pop()
        if (exp_type != bool) ERROR(Type-mismatch)
        else
        result = PilaO.Pop()
        Generate quad: GotoF, result , , ___
        PJumps.Push (cont-1)
        Our Quad_Pointer is always pointing to the
        next quadruple to be generated
        
        2.- end=PJumps.Pop()
        FILL (end, cont)
        
        3.- Generate quad: GOTO ___
        false= PJumps.Pop()
        PJumps.Push(cont-1)
        FILL (false, cont)
        '''



    # ------ WHILE LOOP ------ #
    def p_while_step1(p):
        '''
        1.- PJumps.Push (cont)
        '''

    def p_while_step2(p):
        '''
        2.- exp_type = PTypes.Pop()
        if (exp_type != bool) ERROR(Type-mismatch)
        else
        result = PilaO.Pop()
        Generate quad: GotoF, result , , ___
        PJumps.Push (cont-1)
        '''

    def p_while_step3(p):
        '''
        3.- end=PJumps.Pop()
        return=PJumps.Pop()
        Generate quad: GOTO return
        FILL (end, cont)
        '''


    def p_end_program(self):
        print("Final Symbol Table: ")
        pprint.pprint(memory.symbolTable)
        """ pprint.pprint(memory.symbolTable, indent=4)
        print("O O O O O O")
        print(memory.pTypes)
        print(memory.pNames)
        memory.printSymbolTable() """