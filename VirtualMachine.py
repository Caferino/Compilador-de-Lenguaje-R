"""
    Proyecto Final
    Autor: Óscar Antonio Hinojosa Salum A00821930
    Abril 15 2023
    Compilador para lenguaje al estilo R.

    VM / Virtual Machine
    Input: Cuádruplos en forma de tuplas tipo
    [operador, operandoIzquierdo, operandoDerecho, dondeInsertarResultado]

    Output: Resultados del programa.
"""

import Memory
import pprint
import sys
import re

class VirtualMachine:
    def __init__(self):
        self.registers = []
        self.registers.append("GOTO MAIN")
        self.stack = []
        self.program_counter = 0
        self.quadruples = []
        self.symbolTable = []

    def start(self, quadruples, newSymbolTable):
        self.quadruples = quadruples
        self.symbolTable = newSymbolTable
        self.run()

    def run(self):
        print("It's showtime: ") # ! DEBUG
        pprint.pprint(self.quadruples, stream=sys.stdout) # ! DEBUG


        while self.program_counter < len(self.quadruples):
            print("Entramos al while...")
            quadruple = self.quadruples[self.program_counter]
            operator, operand1, operand2, target = quadruple

            print("BEFORE operator = ", operator)
            print("BEFORE target = ", target)
            print("BEFORE operand1 = ", operand1)
            print("BEFORE operand2 = ", operand2)
            # print("Registers size = ", len(self.registers), "+ 1") # ! DEBUG

            # Qué asco ya sé, una búsqueda lineal O(n) por cada operando que sea una variable...
            # Si nuestro resultado será un espacio temporal, lo "hacemos" índice (t1 = 1, t82 = 82, ...)
            # "t0", al "no existir", lo dejé reservado para el GOTO MAIN por si acaso y mientras
            if isinstance(target, str) and re.match(r"^t\d+$", target) : 
                target = int(target[1:])
                self.registers.append(target)

            # Si nuestro operando izquierdo es un espacio temporal ...
            if isinstance(operand1, str) and re.match(r"^t\d+$", operand1) : 
                operand1 = self.registers[int(operand1[1:])]
                print("Operand1 value = ", operand1)
            # Si no, debe ser un ID cuyo valor debemo sacar de la SymbolTable
            elif isinstance(operand1, str):
                for tuple in self.symbolTable :
                    if operand1 in tuple[1] :
                        operand1 = tuple[6][0]
                        break

            # Si nuestro operando derecho es un espacio temporal ...
            if isinstance(operand2, str) and re.match(r"^t\d+$", operand2) : 
                operand2 = self.registers[int(operand2[1:])]
                print("Operand1 value = ", operand2)
            # Si no, debe ser un ID cuyo valor debemo sacar de la SymbolTable
            elif isinstance(operand2, str):
                for tuple in self.symbolTable :
                    print("QUE SUCEDE = ", operand2)
                    if operand2 in tuple[1] :
                        operand2 = tuple[6][0]
                        break

            # ! DEBUG
            print("AFTER operator = ", operator)
            print("AFTER target = ", target)
            print("AFTER operand1 = ", operand1)
            print("AFTER operand2 = ", operand2)


            # Dios mío bendito. Los famosos registers de Windows que rompen todo
            if operator == '+' :
                self.registers[target] = operand1 + operand2
            elif operator == '-' :
                self.registers[target] = operand1 - operand2
            elif operator == '*' :
                self.registers[target] = operand1 * operand2
            elif operator == '/' :
                self.registers[target] = operand1 / operand2
            elif operator == '>' :
                self.registers[target] = int(operand1 > operand2)
            elif operator == '<' :
                self.registers[target] = int(operand1 < operand2)
            elif operator == '=' or operator == '<-' :
                # Si es un string, es porque a fuerza es un ID ...
                if target.__class__.__name__ == 'str' :
                    print("Actualizar el valor de ", target) # ! DEBUG
                    for i, tuple_item in enumerate(self.symbolTable):
                        if target in tuple_item[1]:
                            
                            currentRow = self.symbolTable[i]
                            # Actualizamos la columna "functionParent"
                            index_to_change = 6
                            currentRow = currentRow[:index_to_change] + (operand1,)
                            self.symbolTable[i] = currentRow
                            print("TUPLA NUEVA ", self.symbolTable[i]) # ! DEBUG

                # Si no, es el index de un espacio temporal
                else:
                    self.registers[target] = operand1
            elif operator.lower() == 'goto':
                self.program_counter = target
                continue
            elif operator.lower() == 'print':
                print("Print = ", operand1)
            elif operator.lower() == 'return':
                return_value = self.registers[operand1]
                self.program_counter = self.stack.pop()
                self.registers[target] = return_value
                continue

            self.program_counter += 1

        print(self.registers)