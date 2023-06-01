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

class VirtualMachine:
    def __init__(self):
        self.registers = [0] * 10  # Example: 10 registers (R0-R9)
        self.stack = []
        self.program_counter = 0
        # TODO - Vaciar pila self.quadruples, la llené con un ejemplo de prueba
        self.quadruples = []

    def start(self, quadruples):
        self.quadruples = quadruples
        self.run()

    def run(self):
        print("It's showtime: ") # ! DEBUG
        pprint.pprint(self.quadruples, stream=sys.stdout) # ! DEBUG


        while self.program_counter < len(self.quadruples):
            quadruple = self.quadruples[self.program_counter]
            operator, operand1, operand2, target = quadruple

            # Dios mío bendito. Los famosos registers de Windows que rompen todo
            """ if operator == '+':
                self.registers[target] = self.registers[operand1] + self.registers[operand2]
            elif operator == '-':
                self.registers[target] = self.registers[operand1] - self.registers[operand2]
            elif operator == '*':
                self.registers[target] = self.registers[operand1] * self.registers[operand2]
            elif operator == '/':
                self.registers[target] = self.registers[operand1] / self.registers[operand2]
            elif operator == '>':
                self.registers[target] = int(self.registers[operand1] > self.registers[operand2])
            elif operator == '<':
                self.registers[target] = int(self.registers[operand1] < self.registers[operand2])
            elif operator == '=':
                self.registers[target] = self.registers[operand1]
            elif operator == '=':
                self.registers[target] = self.registers[operand1] """

            self.program_counter += 1