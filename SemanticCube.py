typeMatchTable = [
    #    OpI   OpD   ^    *    /    %    +    -    >    <   <>   !=   ==    =   &&   ||
    #    ------------------------------------------------------------------
    ['int', 'int', 'int', 'int', 'float', 'int', 'int', 'int', 'bool', 'bool', 'bool', 'bool', 'bool', 'int', 'bool', 'bool'],
    ['int', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'bool', 'bool', 'bool', 'bool', 'bool', 'float', 'bool', 'bool'],
    ['int', 'char', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'bool', 'bool', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],
    ['int', 'bool', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'bool', 'bool', 'bool', 'bool', 'bool', 'bool', 'bool', 'bool'],
    ['float', 'int', 'float', 'float', 'float', 'float', 'float', 'float', 'bool', 'bool', 'bool', 'bool', 'bool', 'float', 'bool', 'bool'],
    ['float', 'float', 'float', 'float', 'float', 'float', 'float', 'float', 'bool', 'bool', 'bool', 'bool', 'bool', 'float', 'bool', 'bool'],
    ['float', 'char', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'bool', 'bool', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],
    ['float', 'bool', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'bool', 'bool', 'bool', 'bool', 'bool', 'bool', 'bool', 'bool'],
    ['char', 'int', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'bool', 'bool', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],
    ['char', 'float', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'bool', 'bool', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],
    ['char', 'char', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'bool', 'bool', 'char', 'ERROR', 'ERROR', 'ERROR'],
    ['char', 'bool', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'bool', 'bool', 'bool', 'bool', 'ERROR', 'ERROR'],
    ['bool', 'int', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'bool', 'bool', 'bool', 'bool', 'bool', 'bool', 'bool', 'bool'],
    ['bool', 'float', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'bool', 'bool', 'bool', 'bool', 'bool', 'bool', 'bool', 'bool'],
    ['bool', 'char', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'bool', 'bool', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],
    ['bool', 'bool', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'bool', 'bool', 'bool', 'bool', 'bool', 'bool']
]

def Semantics(left_Type, right_Type, operator):
    # Checar tipos y regresar tipo
    print("Semantic Cube, baby!")