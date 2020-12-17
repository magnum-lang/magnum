"""
#######################################
                TOKENS
#######################################

Tokens used for lexical analasis and parsing

Ex:
    In: 3
    Out: TOKEN_INT:3
"""

# Primitives
from typing import Union
from magnum.src.position import Position

TT_INT = 'INT'
TT_FLOAT = 'FLOAT'

# Operands
TT_PLUS = 'PLUS'
TT_MINUS = 'MINUS'
TT_MUL = 'MUL'
TT_DIV = 'DIV'

# Other
TT_LPAREN = 'LPAREN'
TT_RPAREN = 'RPAREN'
TT_EOF = 'EOF'


class Token:
    def __init__(self,
                 type_,
                 value=None,
                 pos_start: Union[Position, None] = None,
                 pos_end: Union[Position, None] = None):
        self.type = type_
        self.value = value

        if pos_start:
            self.pos_start: Position = pos_start.copy()
            self.pos_end: Position = pos_start.copy()

            self.pos_end.advance()

        if pos_end:
            self.pos_end: Position = pos_end.copy()

    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'