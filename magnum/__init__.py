from magnum.src.parser import Parser
from magnum.src.lexer import Lexer


def run(fn: str, text: str):
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()

    if error: return None, error

    parser: Parser = Parser(tokens)
    ast = parser.parse()

    return ast, ast.error