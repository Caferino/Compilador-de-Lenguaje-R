"""
    Proyecto Final
    Autor: Óscar Antonio Hinojosa Salum A00821930
    Abril 15 2023
    Compilador para lenguaje al estilo R/C++.

    CR++, El Cristiano Ronaldo de los Lenguajes de Programación.
"""

# ======================== Sintáxis ======================== #

from Semantics import Rules

def p_program(p):
    '''program : block'''
    p[0] = "COMPILED"
    Rules.p_end_program()


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
    Rules.p_vars(p)


def p_type(p):
    '''type : INT
            | FLOAT
            | BOOL
            | VOID'''
    Rules.p_types(p)
    

def p_vars_equals(p):
    '''vars_equals : assignment LEFTCORCH expression array_vars RIGHTCORCH extra_vars
                | assignment LEFTCORCH empty RIGHTCORCH extra_vars
                | assignment expression extra_vars
                | extra_vars
                | empty'''


def p_extra_vars(p):
    '''extra_vars : COMMA ID vars_equals
                | empty'''
    Rules.p_vars(p)


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