"""
    Proyecto Final
    Autor: Óscar Antonio Hinojosa Salum A00821930
    Abril 15 2023
    Compilador para lenguaje al estilo R/C++.

    --- Memoria para la Symbol Table ---
"""

# ======================== Memoria ======================== #

class MemoryMap:
    def __init__(self):
        # self.memory = [None] * size
        self.quadruples = []
        self.symbolTable = []
        

    """
        !insertRow
        * Inserta una nueva tupla a la symbolTable
        ? @param new_row Con formato (type, name)
    """
    def insertRow(self, new_row):
        # Si la Symbol Table está vacía, insertar row sí o sí
        if not self.symbolTable:
            self.symbolTable.append(new_row)

        # Si la Symbol Table NO está vacía, verificar existencia de la variable primero
        else:
            found = False
            for each_existing_tuple in self.symbolTable:
                # Si la variable ya existe, actualizamos solo el value
                if new_row[1] == each_existing_tuple[1]:
                    # ACTUALIZAR VALUE SOLAMENTE
                    # VERIFICAR TIPOS, EJEMPLO: FLOAT Z ... BOOL Z, ¿QUÉ SUCEDE?
                    found = True
                    break

            # Si la variable aún no existe, insertarla
            if not found:
                self.symbolTable.append(new_row)