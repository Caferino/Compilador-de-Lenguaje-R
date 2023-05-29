"""
    Proyecto Final
    Autor: Óscar Antonio Hinojosa Salum A00821930
    Mayo 28 2023
    Compilador para lenguaje al estilo R.

    Constructor de Cuádruplos
"""

import re # Librería para expresiones regulares RegEX
import SemanticCube

class Quadruples:
    def __init__(self):
        # Mom
        self.quadruples = []
        self.quad_count = 0

        # Pilas para construir cuádruplos
        self.PilaO = []
        self.PTypes = []
        self.POper = []


    # ------ 1. Insertando Type y ID ------ #
    def insertTypeAndID(self, token):
        self.PilaO.append(token)
        self.PTypes.append(token.__class__.__name__)


    # ------ 2 y 3. Insertando Signos (+, -, *, /, <, >, <>, =, ...) ------ #
    def insertSign(self, token):
        
        self.POper.append(token)
        print("Entramos a insertSign alright: ", self.POper[-1])
    

    # ------ 4. Verificando Sumas o Restas ------ #
    def verifySignPlusOrMinus(self):
        # print("Current POper: ", self.POper)
        if self.POper:
            if self.POper[-1] == '+' or self.POper[-1] == '-':
                # Asignamos operandos y operador a validar y ejecutar
                # ! IMPORTANTE: El orden de los .pop() importan!
                right_operand = self.PilaO.pop()
                left_operand = self.PilaO.pop()

                right_Type = self.PTypes.pop()
                left_Type = self.PTypes.pop()

                operator = self.POper.pop()
                result_Type = SemanticCube.Semantics(left_Type, right_Type, operator)

                if(result_Type != 'ERROR'):
                    result = 'AVAIL.next()'
                    self.generateQuadruple(operator, left_operand, right_operand, result)
                    self.PilaO.append(result)
                    self.PTypes.append(result_Type)
                    # "If any operand were a temporal space, return it to AVAIL"

                else:
                    raise TypeError("Type mismatch in: ", left_operand, " ", operator, " ", right_operand)


    # ------ 5. Verificando Multiplicaciones o Divisiones ------ #
    def verifySignTimesOrDivide(self):
        # print("Current POper: ", self.POper)
        if self.POper:
            if self.POper[-1] == '*' or self.POper[-1] == '/':
                # Asignamos operandos y operador a validar y ejecutar
                # ! IMPORTANTE: El orden de los .pop() importan!
                right_operand = self.PilaO.pop()
                left_operand = self.PilaO.pop()

                right_Type = self.PTypes.pop()
                left_Type = self.PTypes.pop()

                operator = self.POper.pop()
                result_Type = SemanticCube.Semantics(left_Type, right_Type, operator)

                if(result_Type != 'ERROR'):
                    result = 'AVAIL.next()'
                    self.generateQuadruple(operator, left_operand, right_operand, result)
                    self.PilaO.append(result)
                    self.PTypes.append(result_Type)
                    # "If any operand were a temporal space, return it to AVAIL"

                else:
                    raise TypeError("Type mismatch in: ", left_operand, " ", operator, " ", right_operand)


    # ------ Generador de Cuádruplo ------ #
    def generateQuadruple(self, operator, left_operand, right_operand, result):
        
        # Generar quad

        # Empujamos el nuevo cuádruple a nuestra lista o memoria
        self.quadruples.append('quad')

    
    def debugger(self):
        # print("PilaO: ", self.PilaO)
        # print("PTypes: ", self.PTypes)
        # print("POper: ", self.POper)
        print("Quadruples: ", self.quadruples)

quadsConstructor = Quadruples()