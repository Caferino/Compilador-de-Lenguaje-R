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

import pprint
import sys
import re

class VirtualMachine:
    def __init__(self):
        self.registers = {}
        self.stack = []
        self.program_counter = 0
        self.quadruples = []

    def start(self, quadruples):
        self.quadruples = quadruples
        self.run()

    def run(self):
        print("It's showtime: ") # ! DEBUG
        pprint.pprint(self.quadruples, stream=sys.stdout) # ! DEBUG


        while self.program_counter < len(self.quadruples):
            print("Entramos al while...")
            quadruple = self.quadruples[self.program_counter]
            operator, operand1, operand2, target = quadruple

            print("operator = ", operator)
            print("target = ", target)
            print("operand1 = ", operand1)
            print("operand2 = ", operand2)

            if re.match(r"^t\d+$", target) : target = int(target[1:])
            """ if operand1.__class__.__name__ == 'str' : operand1 = int(operand1[1:])
            if operand2.__class__.__name__ == 'str' : operand2 = int(operand2[1:]) """

            # Dios mío bendito. Los famosos registers de Windows que rompen todo
            if operator == '+':
                self.registers[target] = operand1 + operand2
            elif operator == '-':
                self.registers[target] = operand1 - operand2
            elif operator == '*':
                self.registers[target] = operand1 * operand2
            elif operator == '/':
                self.registers[target] = operand1 / operand2
            elif operator == '>':
                self.registers[target] = int(operand1 > operand2)
            elif operator == '<':
                self.registers[target] = int(operand1 < operand2)
            elif operator == '=' or operator == '<-':
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