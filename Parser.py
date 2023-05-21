"""
    Proyecto Final
    Autor: Óscar Antonio Hinojosa Salum A00821930
    Abril 15 2023
    Compilador para lenguaje al estilo R.
"""

# ======================== Reglas de Semántica ======================== #

from Memory import MemoryMap

memory = MemoryMap()

# ------ VARIABLES ------ #
def p_varsEnter(p):
    memory.types.append(p[1])
    memory.varsDir.append(p[2])
    # print("Checkpoint") # Debug
    # print(p) # Debug
    # print(p[1], p[2], p[3]) # Debug



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



# ======================== Sintáxis Estilo R ======================== #

from Semantics import Rules

def p_program(p):
    '''program : block'''
    p[0] = "COMPILED"


def p_block(p):
    '''block : vars block
                | statement block
                | empty'''


# Si se llega a pedir matrices cúbicas o más, 
# tal vez pueda ciclarlo aquí y ver cómo sería al guardar en memoria.
# Por ahora solo me interesan las de una o dos dimensiones.
def p_vars(p):
    '''vars : type ID vars_equals SEMICOLON
            | type ID LEFTBRACKET CTEI RIGHTBRACKET vars_equals SEMICOLON
            | type ID LEFTBRACKET CTEI RIGHTBRACKET LEFTBRACKET CTEI RIGHTBRACKET vars_equals SEMICOLON'''
    
    # Lectura de datos según el tamaño del array
    if len(p) == 5:
        # Declaración de una variable
        var_type = p[1]
        var_name = p[2]
        var_size = None
        var_dimensions = None
        var_assignment = p[3]
        print(p[1])
        print(p[2])
        print(p[3])
        print(p[4])
        print(len(p)) # Debug
        print("Len 5 Checkpoint") # DEBUG
        print(var_type)
        print(var_name)
        print(var_size)
        print(var_dimensions)
        print(var_assignment)
    elif len(p) == 8:
        # Array con una dimensión
        var_type = p[1]
        var_name = p[2]
        var_size = p[4]
        var_dimensions = 1
        var_assignment = p[6]
        print("Len 8 Checkpoint") # DEBUG
    elif len(p) == 11:
        # Matrices
        var_type = p[1]
        var_name = p[2]
        var_size = [p[4], p[8]]
        var_dimensions = 2
        var_assignment = p[10]
        print("Len 11 Checkpoint") # DEBUG
    elif len(p) == 10:
        # Matriz con rango de tamaño
        var_type = p[1]
        var_name = p[2]
        var_size = [p[4], p[6]]
        var_dimensions = 2
        var_assignment = p[8]
        print("Len 10 Checkpoint") # DEBUG

    print("===========================") # DEBUG
    
    Rules.p_varsEnter(p)

def p_type(p):
    '''type : INT
            | FLOAT
            | BOOL
            | VOID'''
    

def p_vars_equals(p):
    '''vars_equals : assignment LEFTCORCH expression array_vars RIGHTCORCH extra_vars
                | assignment expression extra_vars
                | extra_vars
                | empty'''


def p_extra_vars(p):
    '''extra_vars : COMMA ID vars_equals
                | empty'''


def p_array_vars(p):
    '''array_vars : COMMA expression array_vars
                | empty'''


def p_sign(p):
    '''sign : PLUS
            | MINUS
            | empty'''


def p_var_cte(p):
    '''var_cte : ID
               | CTEI
               | CTEF'''


def p_statement(p):
    '''statement : function
                 | assignment_block
                 | expression
                 | function_call
                 | loop
                 | condition
                 | writing
                 | empty'''


def p_function(p):
    '''function : type ID LEFTPAREN function_parameters RIGHTPAREN LEFTCORCH block RIGHTCORCH
                | empty'''

    print(" ===== FUNCTION ===== ")
    print(p[1])
    print(p[2])
    print(p[3])
    print(p[4])
    print(p[5])
    print(p[6])
    print(p[7])
    print(p[8])
    print(len(p))
    print(" === END OF FUNCTION === ")



def p_function_parameters(p):
    '''function_parameters : type ID function_extra_parameters'''


def p_function_extra_parameters(p):
    '''function_extra_parameters : COMMA function_parameters
                | empty'''


def p_assignment_block(p):
    '''assignment_block : ID assignment expression SEMICOLON'''


def p_assignment(p):
    '''assignment : ASSIGNL
                 | EQUALS'''


def p_function_call(p):
    '''function_call : ID LEFTPAREN expression function_call_expressions RIGHTPAREN'''


def p_function_call_expressions(p):
    '''function_call_expressions : COMMA function_call_expressions
                 | empty'''


def p_loop(p):
    '''loop : WHILE LEFTPAREN expression RIGHTPAREN LEFTCORCH block RIGHTCORCH
                 | empty'''


def p_condition(p):
    '''condition : IF LEFTPAREN expression RIGHTPAREN LEFTCORCH block RIGHTCORCH else_condition'''


def p_else_condition(p):
    '''else_condition : ELSE LEFTCORCH block RIGHTCORCH
                      | empty'''


def p_writing(p):
    '''writing : PRINT LEFTPAREN print_val RIGHTPAREN SEMICOLON'''


def p_print_val(p):
    '''print_val : expression print_exp
                 | CTESTRING print_exp'''


def p_print_exp(p):
    '''print_exp : COMMA  print_val
                 | empty'''


def p_expression(p):
    '''expression : exp comparation'''


def p_exp(p):
    '''exp : term operator'''


def p_comparation(p):
    '''comparation : AND exp
                 | OR exp
                 | GREATER exp
                 | LESS exp
                 | NOTEQUAL exp
                 | NOTEQUALNUM exp
                 | empty'''


def p_term(p):
    '''term : factor term_operator'''


def p_operator(p):
    '''operator : PLUS term operator
                | MINUS term operator
                | empty'''


def p_term_operator(p):
    '''term_operator : TIMES factor term_operator
                     | DIVIDE factor term_operator
                     | MODULUS factor term_operator
                     | empty'''


def p_factor(p):
    '''factor : LEFTPAREN expression RIGHTPAREN
              | sign var_cte'''




# # ======================== Reglas de Errores ======================== #

def p_error(p):
    print("Syntax error in input! - {} ".format(p))


def p_empty(p):
    '''empty :'''
    pass



# = = = = = = = = = = = = = Main - Lector de Archivos = = = = = = = = = = = = = #

import sys
import ply.yacc as yacc

from Lexer import tokens

yacc.yacc()

if __name__ == '__main__':

    if len(sys.argv) > 1:
        file = sys.argv[1]
        try:
            f = open(file, 'r')
            data = f.read()
            f.close()
            if yacc.parse(data) == "COMPILED":
                # print(data)
                print("Compilation Completed")
        except EOFError:
            print(EOFError)
    else:
        print("File not found")