from antlr4 import *
from gen.JavaLexer import JavaLexer
from gen.JavaParser import JavaParser
from gen.JavaParserVisitor import JavaParserVisitor

def main():
    input_stream = FileStream('input.java')
    lexer = JavaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JavaParser(stream)
    tree = parser.compilationUnit()
    visitor = MethodBodyVisitor(parser._input.tokens)
    visitor.visit(tree)
    with open('output.java', 'w') as f:
        for i in range(1, len(visitor.tokens)):
            if visitor.tokens[i].type != -1:
                f.write(visitor.tokens[i].text)


class MethodBodyVisitor(JavaParserVisitor):
    def __init__(self, tokens):
        super().__init__()
        self.tokens = tokens


    def visitMethodDeclaration(self, ctx:JavaParser.MethodDeclarationContext):
        if ctx.methodBody().getText().strip() == "{}":
            ctx.methodBody().start.text = "{throw new UnsupportedOperationException();}"
            ctx.methodBody().stop.text = ""

        return self.visitChildren(ctx)


if __name__ == '__main__':
    main()
