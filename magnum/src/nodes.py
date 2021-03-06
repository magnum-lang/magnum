from magnum.utils.imports import *


class NumberNode:
    def __init__(self, tok: Token) -> None:
        self.tok: Token = tok

    def __repr__(self) -> str:
        return f'{self.tok}'


class BinOpNode:
    def __init__(self, left_node, op_tok, right_node) -> None:
        self.left_node = left_node
        self.op_tok = op_tok
        self.right_node = right_node

    def __repr__(self) -> str:
        return f'({self.left_node}, {self.op_tok}, {self.right_node})'


class UnaryOpNode:
    def __init__(self, op_tok, node) -> None:
        self.op_tok = op_tok
        self.node = node

    def __repr__(self) -> str:
        return f'({self.op_tok}, {self.node})'