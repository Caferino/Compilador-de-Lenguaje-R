"""
    Proyecto Final
    Autor: Óscar Antonio Hinojosa Salum A00821930
    Abril 15 2023
    Compilador para lenguaje al estilo R/C++.

    CR++, El Cristiano Ronaldo de los Lenguajes de Programación.
"""

# ======================== Sintáxis ======================== #

from Semantics import Rules
from Quadruples import Quadruples

rules = Rules()
quadsConstructor = Quadruples()

def p_program(p):
    '''program : block'''
    p[0] = "COMPILED"
    rules.p_end_program()
    quadsConstructor.debugger()


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
    # Semántica
    rules.p_insertID(p, False)


def p_type(p):
    '''type : INT
            | FLOAT
            | BOOL
            | VOID'''
    rules.p_insertType(p)
    

def p_vars_equals(p):
    '''vars_equals : assignment vars_equals_array extra_vars
                | assignment expression extra_vars
                | extra_vars
                | empty'''


def p_vars_equals_array(p):
    '''vars_equals_array : LEFTCORCH expression array_vars RIGHTCORCH
                | LEFTCORCH empty RIGHTCORCH'''
    rules.p_saveValue(p)


def p_extra_vars_comma(p):
    '''extra_vars_comma : COMMA'''
    rules.p_saveComma(p)


def p_extra_vars(p):
    '''extra_vars : extra_vars_comma ID vars_equals
                | empty'''
    rules.p_insertID(p, False)


def p_array_vars(p):
    '''array_vars : COMMA expression array_vars
                | empty'''


def p_sign(p):
    '''sign : PLUS
            | MINUS
            | empty'''
    rules.p_saveSign(p)


def p_var_cte(p):
    '''var_cte : ID
               | CTEI
               | CTEF'''
    # PROBLEMA CON SALSA
    # Semántica
    rules.p_saveValue(p)
    rules.p_saveToOpStack(p)

    # Cuádruplos
    quadsConstructor.insertTypeAndID(p[1])


def p_statement(p):
    '''statement : function
                 | assignment_block
                 | expression
                 | function_call
                 | loop
                 | condition
                 | writing
                 | empty'''
    rules.p_saveToOpStack(p)


def p_function(p):
    '''function : type ID LEFTPAREN function_parameters RIGHTPAREN LEFTCORCH block RIGHTCORCH
                | empty'''
    rules.p_insertScope('global')
    rules.p_registerLocalVariables(p)
    rules.p_insertID(p, True)


def p_function_parameters(p):
    '''function_parameters : type ID function_extra_parameters
                | empty'''
    rules.p_insertScope('local')
    rules.p_saveLocalVariable(p)
    rules.p_insertID(p, False)


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
                print("Compilation Completed")
        except EOFError:
            print(EOFError)
    else:
        print("File not found")