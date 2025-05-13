from dyno.lexer import tokenize
from dyno.parser import parse
from dyno.interpreter import execute

def run_dyno_code(code):
    tokens = tokenize(code)
    ast = parse(tokens)
    execute(ast)

if _name_ == "_main_":
    with open("tests/test_cases.dyno") as file:
        code = file.read()
        run_dyno_code(code)
