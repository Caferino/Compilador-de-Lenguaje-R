"""
    Proyecto Final
    Autor: Óscar Antonio Hinojosa Salum A00821930
    Mayo 28 2023
    Compilador para lenguaje al estilo R.

    Constructor de Cuádruplos
"""

import re # Librería para expresiones regulares RegEX
from Memory import MemoryMap
import pprint # Para imprimir el Symbol Table de manera bonita

memory = MemoryMap()

class Quadruples:
    def __init__(self):
        # Mom
        self.quadruples = []
        self.quad_count = 0

        # Pilas para construir cuádruplos
        self.PilaO = []
        self.PTypes = []
        self.POper = []

        # Auxiliares
        self.left_operand = None
        self.right_operand = None
        self.left_Type = None
        self.right_Type = None




    # ------ 1. Inserting Type and ID ------ #
    def insertTypeAndID(self, p):
        self.placeHolder = None


    # ------ 1. Inserting Type and ID ------ #
    def generateQuadruple(self, operator, operand1, operand2, result):
        quadruple = (operator, operand1, operand2, result)
        self.quadruples.append(quadruple)
        self.quad_count += 1

    
    def debugger(self):
        # print("PilaO: ", self.PilaO)
        # print("PTypes: ", self.PTypes)
        # print("POper: ", self.POper)
        print("Quadruples: ", self.quadruples)