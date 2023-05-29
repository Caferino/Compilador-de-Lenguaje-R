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

        # Para los estatutos que requieren saltos
        self.PJumps = []
        self.cont = 1  ## Los cuádruplos empiezan desde 1.





    # ------------------ EXPRESIONES LINEALES ------------------ #
    # ------ 1. Insertando Type y ID ------ #
    def insertTypeAndID(self, token):
        self.PilaO.append(token)
        self.PTypes.append(token.__class__.__name__)
        # ! TODO: Si es un ID, que saque su tipo real, valor también tal vez, etc.
        # ! Espérate al error del Semantic Cube


    # ------ 2 y 3. Insertando Signos (+, -, *, /, <, >, <>, =, ...) ------ #
    def insertSign(self, token):
        
        self.POper.append(token)
        print("Entramos a insertSign alright: ", self.POper[-1])
    

    # ------ 4. Verificando Sumas o Restas ------ #
    def verifySignPlusOrMinus(self):
        # print("Current POper: ", self.POper) # ! DEBUG
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
                    result = 'AVAIL.next()'  # TODO Lógica de AVAIL
                    self.generateQuadruple(operator, left_operand, right_operand, result)
                    self.PilaO.append(result)
                    self.PTypes.append(result_Type)
                    # TODO: "If any operand were a temporal space, return it to AVAIL"

                else:
                    print("Type mismatch in: ", left_operand, operator, right_operand)


    # ------ 5. Verificando Multiplicaciones o Divisiones ------ #
    def verifySignTimesOrDivide(self):
        # print("Current POper: ", self.POper) # ! DEBUG
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
                    result = 'AVAIL.next()'  # TODO Lógica de AVAIL
                    self.generateQuadruple(operator, left_operand, right_operand, result)
                    self.PilaO.append(result)
                    self.PTypes.append(result_Type)
                    # TODO: "If any operand were a temporal space, return it to AVAIL"

                else:
                    print("Type mismatch in: ", left_operand, operator, right_operand)





    # ------------------ CONDICIONALES ------------------ #
    # ------ 1. Primer nodo de un IF/ELSE statement ------ #
    def nodoCondicionalUno(self):
        exp_type = self.PTypes.pop()
        if(exp_type != 'bool') : print("Type Mismatch in a Conditional!", exp_type, "in", self.quadruples)
        else:
            result = self.PilaO.pop()
            self.generateQuadruple('GotoF', result, '', 'linePlaceHolder')
            self.PJumps.append(self.cont - 1)


    # ------ 2. Segundo nodo de IF/ELSE  ------ #
    def nodoCondicionalDos(self):
        end = self.PJumps.pop()
        # TODO: FILL(end, self.cont)


    # ------ 3. Tercer nodo de IF/ELSE  ------ #
    def nodoCondicionalTres(self):
        false = self.PJumps.pop()
        self.PJumps.push(self.cont - 1)
        # TODO: FILL(false, self.cont)





    # ------------------ CICLOS WHILE ------------------ #
    # ------ 1. Primer nodo de un WHILE statement ------ #
    def nodoWhileUno(self):
        self.PJumps.append(self.cont)


    # ------ 2. Segundo nodo de WHILE ------ #
    def nodoWhileDos(self):
        exp_type = self.PTypes.pop()
        if(exp_type != 'bool') : print("Type Mismatch in a While Loop!", exp_type, "in", self.quadruples)
        else:
            result = self.PilaO.pop()
            self.generateQuadruple('GotoF', result, '', 'linePlaceHolder')
            self.PJumps.push(self.cont - 1)


    # ------ 3. Tercer nodo de WHILE ------ #
    def nodoWhileTres(self):
        end = self.PJumps.pop()
        varReturn = self.PJumps.pop()
        self.generateQuadruple('GOTO', varReturn, '', '')
        # TODO: FILL(end, self.cont)





    # ------------------ MÉTODOS AUXILIARES ------------------ #
    # ------ Generador de Cuádruplos ------ #
    def generateQuadruple(self, operator, left_operand, right_operand, result):
        
        # TODO Generar cuádruplo tipo quad = (operator, left_operand, right_operand, result)
        # quad = (operator, left_operand, right_operand, result)
        # print("QUAD ACTUAL: ", quad) # ! DEBUG

        # Empujamos el nuevo cuádruple a nuestra lista o memoria
        self.quadruples.append('quad')

    
    def debugger(self):
        # print("PilaO: ", self.PilaO)
        # print("PTypes: ", self.PTypes)
        # print("POper: ", self.POper)
        print("Quadruples: ", self.quadruples)

quadsConstructor = Quadruples()