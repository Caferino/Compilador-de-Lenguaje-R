"""
    Proyecto Final
    Autor: Óscar Antonio Hinojosa Salum A00821930
    Abril 15 2023
    Compilador para lenguaje al estilo R.

    Reglas de Semántica
"""

from Memory import MemoryMap

memory = MemoryMap()

class Rules:
    # ------ TYPES ------ #
    def p_types_Rule1(p):
        print(p[1])

    # ------ VARIABLES ------ #
    def p_vars_Rule1(p):
        if len(p) == 5:
            # DECLARACIÓN DE MATRICES
            if "[" in p[2]:
                varNameIndex = p[2].index('[')
                varName = p[2][:varNameIndex]
                print(varName)

            # DECLARACIÓN DE UNA VARIABLE
            else:
                print(p[2]) # "varName"

            
            # print(p[3]) # None
            print(p[4])
            print("Length = ", len(p)) # Debug
        print("===========================") # DEBUG
        # memory.types.append(p[1])
        # memory.varsDir.append(p[2])
        # print("Checkpoint") # Debug
        # print(p) # Debug
        # print(p[1], p[2], p[3]) # Debug
        # Lectura de datos según el tamaño del array



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