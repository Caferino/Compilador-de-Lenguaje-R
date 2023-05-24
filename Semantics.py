"""
    Proyecto Final
    Autor: Óscar Antonio Hinojosa Salum A00821930
    Abril 15 2023
    Compilador para lenguaje al estilo R.

    Reglas de Semántica
"""

# ======================== Semántica ======================== #

import re # Librería para expresiones regulares RegEX
from Memory import MemoryMap
import pprint # Para imprimir el Symbol Table de manera bonita

memory = MemoryMap()
new_row = {}

class Rules:
    # ------ TYPES ------ #
    def p_types(p):
        new_row['type'] = p[1]



    # ------ VARIABLES ------ #
    def p_vars(p):
        # DECLARACIÓN DE MATRICES
        if len(p) == 5:
            # Separar nombre de la matriz de sus dimensiones
            if "[" in p[2]:
                varNameIndex = p[2].index('[')
                varName = p[2][:varNameIndex]
                print(varName)
                new_row['name'] = varName
                # Lo mandamos a memoria, donde se verifica si existe o no (actualizamos solo el value si sí)
                memory.insertRow(new_row)
                # Extraemos las dimensiones de los brackets a una lista
                indices = re.findall(r'\[(.*?)\]', p[2])
                # Tranformar de strings a integers ['1', '2', ...] -> [1, 2, ...]
                indices = [int(index) for index in indices]
                print(indices)

            # DECLARACIÓN DE UNA VARIABLE
            else:
                print(p[2]) # "varName"
                varName = p[2]
                new_row['name'] = varName
                # VERIFICAR QUE YA EXISTE
                memory.insertRow(new_row)

            
            # print(p[3]) # None
            print(p[4]) # ;
            print("Length = ", len(p)) # Debug
        
        if len(p) == 4:
            if "[" in p[2]:
                # Separamos el nombre de la matriz de sus dimensiones
                varNameIndex = p[2].index('[')
                varName = p[2][:varNameIndex]
                print(varName)
                new_row['name'] = varName
                # VERIFICAR QUE YA EXISTE
                memory.insertRow(new_row)
                # Extraemos las dimensiones de los brackets a una lista
                indices = re.findall(r'\[(.*?)\]', p[2])
                # Tranformar de strings a integers ['1', '2', ...] -> [1, 2, ...]
                indices = [int(index) for index in indices]
                print(indices)
            
            else:
                print(p[2])
                varName = p[2]
                new_row['name'] = varName
                # VERIFICAR QUE YA EXISTE
                memory.insertRow(new_row)

        print("Current Row Count: ", memory.rowCount)
        print("===========================") # DEBUG



    # ------ FUNCTION ------ #
    def p_function(p):
        '''
        1.- Insert Procedure name into the DirFunc table, verify semantics.

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

        6.- Generate action GOSUB, procedure-name, , initial-address
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


    def p_end_program():
        pprint.pprint(memory.symbolTable, indent=4)