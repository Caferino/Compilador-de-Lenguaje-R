# coding=utf-8
"""
    Proyecto Final
    Autor: Óscar Antonio Hinojosa Salum A00821930
    Abril 15 2023
    Compilador para lenguaje al estilo R.
"""

# Sintáxis Estilo R

def p_program(p):
    '''program : block'''
    p[0] = "COMPILED"


def p_block(p):
    '''block : vars block
                | statement block
                | empty'''


def p_vars(p):
    '''vars : type ID vars_equals SEMICOLON vars
            | empty'''


def p_type(p):
    '''type : INT
            | FLOAT
            | VOID'''
    

def p_vars_equals(p):
    '''vars_equals : EQUALS var_cte extra_vars
                | ASSIGNL var_cte extra_vars
                | empty'''
                

def p_extra_vars(p):
    '''extra_vars : COMMA ID extra_vars
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
    '''statement : assignment_block
                 | module
                 | expression
                 | function_call
                 | loop
                 | condition
                 | writing
                 | empty'''


"""
def p_function(p):
    '''function : type ID LEFTPAREN parameters RIGHTPAREN LEFTCORCH block RIGHTCORCH'''
"""


def p_assignment_block(p):
    '''assignment_block : ID assignment expression SEMICOLON'''


def p_assigment(p):
    '''assignment : EQUALS
                 | ASSIGNL'''


def p_module(p):
    '''module : VOID ID LEFTPAREN module_params RIGHTPAREN block SEMICOLON
                 | empty'''


def p_function_call(p):
    '''function_call : ID LEFTPAREN expression function_call_expressions RIGHTPAREN'''


def p_function_call_expressions(p):
    '''function_call_expressions : COMMA function_call_expressions
                 | empty'''


def p_module_params(p):
    '''module_params : type ID module_extra_params'''


def p_module_extra_params(p):
    '''module_extra_params : COMMA type ID module_extra_params
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
    '''comparation : GREATER exp
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
                     | empty'''


def p_factor(p):
    '''factor : LEFTPAREN expression RIGHTPAREN
              | sign var_cte'''


# Reglas de Errores

def p_error(p):
    print("Syntax error in input! - {} ".format(p))


def p_empty(p):
    '''empty :'''
    pass


# Programa Principal - lector de archivos ".txt"

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



"""
def p_expression(p):
    '''expression : exp comparation'''


def p_exp(p):
    '''exp : term operator'''


def p_comparation(p):
    '''comparation : GREATER exp
                      | LESS exp
                      | NOTEQUAL exp
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
                     | empty'''


def p_factor(p):
    '''factor : LEFTPAREN expression RIGHTPAREN
              | sign var_cte'''


def p_sign(p):
    '''sign : PLUS
            | MINUS
            | empty'''


def p_var_cte(p):
    '''var_cte : ID
               | CTEI
               | CTEF'''

"""

"""
def p_statement(p):
    '''statement : assignment_block
                 | loop
                 | condition
                 | writing
                 | empty'''


def p_assignment_block(p):
    '''assignment_block : assignment expression SEMICOLON'''


def p_assigment(p):
    '''assignment : EQUALS
                 | ASSIGNL'''


def p_loop(p):
    '''loop : WHILE LEFTPAREN expression RIGHTPAREN LEFTCORCH block RIGHTCORCH'''


def p_condition(p):
    '''condition : IF LEFTPAREN expression RIGHTPAREN block else_condition SEMICOLON'''


def p_else_condition(p):
    '''else_condition : ELSE block
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
    '''comparation : GREATER exp
                      | LESS exp
                      | NOTEQUAL exp
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
                     | empty'''


def p_factor(p):
    '''factor : LEFTPAREN expression RIGHTPAREN
              | sign var_cte'''


def p_sign(p):
    '''sign : PLUS
            | MINUS
            | empty'''


def p_var_cte(p):
    '''var_cte : ID
               | CTEI
               | CTEF'''


"""