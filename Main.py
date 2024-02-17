from flask import Flask
from flask import request
from antlr4 import *
import json

from antlr.generated.ExprParser import ExprParser
from antlr.generated.ExprLexer import ExprLexer
from language.context.ContextManager import ContextManager
from language.context.Data import Data
from language.initializer.Initializer import Initializer
from language.resolvers.ResolverRegistry import ResolverRegistry

app = Flask(__name__)


def main():
    with open("data.json") as f:
        nested_json = f.read()

    # Parse JSON string to a Python dictionary
    data = json.loads(nested_json)

    with open("rating/spire/HO/client/ho-rating.txt") as p:
        program = p.read()

    # memory = {"__current": data, "RETURN": False, "CONTINUE": False, "BREAK": False}
    contextmanager = ContextManager()
    contextmanager.getmemory().add("__current", Data(data))
    Initializer()

    lexer = ExprLexer(InputStream(program))
    tokens = CommonTokenStream(lexer)
    parser = ExprParser(tokens)
    tree = parser.prog()
    # print(tree.toStringTree(recog=parser))
    ResolverRegistry().get(tree.__class__.__name__).resolve(tree, contextmanager)


@app.route("/rating/acord/<lob>/<client>", methods=['POST'])
def acord_rating(client, lob):
    with open(f"rating/acord/{lob}/{client}/ho-rating.txt") as p:
        program = p.read()
    memory = {"__current": request.json, "RETURN": False, "CONTINUE": False, "BREAK": False}
    Initializer()

    lexer = ExprLexer(InputStream(program))
    tokens = CommonTokenStream(lexer)
    parser = ExprParser(tokens)
    tree = parser.prog()
    ResolverRegistry().get(tree.__class__.__name__).resolve(tree, memory)
    return request.json


@app.route("/rating/spire/<lob>/<client>", methods=['POST'])
def spire_rating(client, lob):
    with open(f"rating/spire/{lob}/{client}/ho-rating.txt") as p:
        program = p.read()
    memory = {"__current": request.json, "RETURN": False, "CONTINUE": False, "BREAK": False}
    Initializer()

    lexer = ExprLexer(InputStream(program))
    tokens = CommonTokenStream(lexer)
    parser = ExprParser(tokens)
    tree = parser.prog()
    ResolverRegistry().get(tree.__class__.__name__).resolve(tree, memory)
    return request.json


if __name__ == '__main__':
    # app.run(port=8181)
    main()
