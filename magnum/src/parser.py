from magnum.src.error import InvalidSyntaxError
from magnum.utils.imports import *
from magnum.src.nodes import *
from typing import List, Union

class ParseResult:
    def __init__(self) -> None:
        self.error: Union[InvalidSyntaxError, None] = None
        self.node = None

    def register(self, res: Token):
        if isinstance(res, ParseResult):
            if res.error: self.error = res.error
            return res.node

        return res

    def success(self, node: Union[NumberNode, UnaryOpNode, BinOpNode]):
        self.node = node
        return self

    def failure(self, error: InvalidSyntaxError):
        self.error = error
        return self

    def __repr__(self) -> str:
        return f'{self.node}'


class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.tok_idx = -1
        self.advance()

    def advance(self) -> Token:
        self.tok_idx += 1
        if self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]
        return self.current_tok

    def factor(self) -> ParseResult:
        res = ParseResult()
        tok = self.current_tok

        if tok.type in (TT_PLUS, TT_MINUS):
            res.register(self.advance())
            factor = res.register(self.factor())
            if res.error: return res
            return res.success(UnaryOpNode(tok, factor))

        elif tok.type in (TT_INT, TT_FLOAT):
            res.register(self.advance())
            return res.success(NumberNode(tok))

        elif tok.type == TT_LPAREN:
            res.register(self.advance())
            expr = res.register(self.expr())
            if res.error: return res

            if self.current_tok.type == TT_RPAREN:
                res.register(self.advance())
                return res.success(expr)
            else:
                return res.failure(
                    InvalidSyntaxError(self.current_tok.pos_start,
                                       self.current_tok.pos_end,
                                       "Expected ')'"))

        return res.failure(
            InvalidSyntaxError(tok.pos_start, tok.pos_end,
                               "Expected int or float"))

    def parse(self):
        res = self.expr()
        if not res.error and self.current_tok.type != TT_EOF:
            return res.failure(
                InvalidSyntaxError(self.current_tok.pos_start,
                                   self.current_tok.pos_end,
                                   "Expected '+', '-', '*' or '/'"))

        return res

    def term(self) -> ParseResult:
        return self.bin_op(self.factor, (TT_MUL, TT_DIV))

    def expr(self) -> ParseResult:
        return self.bin_op(self.term, (TT_PLUS, TT_MINUS))

    def bin_op(self, rule, ops) -> ParseResult:
        res = ParseResult()
        left = res.register(rule())

        if res.error: return res

        while self.current_tok.type in ops:
            op_tok = self.current_tok
            res.register(self.advance())
            right = res.register(rule())

            if res.error: return res

            left = BinOpNode(left, op_tok, right)
            self.advance()

        return res.success(left)
