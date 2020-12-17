"""
#######################################
               ERRORS
#######################################

All errors represented by Magnum
Ex:
    magnum>>> 3 $ 4
                ^

Syntax Error at line 1 `<stdin>`
"""
from magnum.utils.string_with_arrows import string_with_arrows
from magnum.src.position import *


class BaseError:
    def __init__(self, pos_start: Position, pos_end: Position, error_name: str,
                 details: str):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details

    def __str__(self):
        result = f'{self.error_name}: {self.details}\n'
        result += f'File {self.pos_start.fn}, line {self.pos_start.ln + 1}'
        result += '\n' + string_with_arrows(self.pos_start.ftxt,
                                            self.pos_start, self.pos_end)

        return result


class IllegalCharError(BaseError):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Illegal Character', details)


class InvalidSyntaxError(BaseError):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Illegal Syntax', details)