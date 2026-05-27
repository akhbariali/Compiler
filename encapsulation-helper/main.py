from antlr4 import *
from gen.JavaLexer import JavaLexer
from gen.JavaParser import JavaParser
from gen.JavaParserVisitor import JavaParserVisitor

def getsetadd(input_file):

    with open(input_file, 'r') as file:
        java_code = file.read()
    lexer = JavaLexer(InputStream(java_code))
    stream = CommonTokenStream(lexer)
    parser = JavaParser(stream)
    tree = parser.compilationUnit()
    visitor = MyClassVisitor()
    visitor.visit(tree)
    output = ""
    for field_type, field_name, is_final in visitor.private_fields:
        output += f"    private {field_type} {field_name};\n"
        methods = visitor.getsetgen(field_type, field_name, is_final)
        output += f"{methods}\n"
    if output:
        output = f"public class Sample {{\n{output}}}"

    with open('output.java', 'w') as file:
        file.write(output)


class MyClassVisitor(JavaParserVisitor):
    def __init__(self):
        self.private_fields = []

    def visitClassBodyDeclaration(self, ctx: JavaParser.ClassBodyDeclarationContext):
        modifiers = ctx.modifier()
        is_private = False
        is_final = False
        for modifier in modifiers:
            modifier_text = modifier.classOrInterfaceModifier().getText()
            if modifier_text == "private":
                is_private = True
            if modifier_text == "final":
                is_final = True
        fielddec = ctx.memberDeclaration().fieldDeclaration()
        field_type = fielddec.typeType().getText()
        field_name = fielddec.variableDeclarators().getText()
        if is_private:
            self.private_fields.append((field_type, field_name, is_final))

    def getsetgen(self, field_type, field_name, is_final):
        namget = "get" + field_name.capitalize()
        getmet = f"\tpublic {field_type} {namget}()\n\t{{\n\t\treturn {field_name};\n\t}}"
        if not is_final:
            setter_name = "set" + field_name.capitalize()
            setter_method = f"\tpublic void {setter_name}({field_type} value) \n\t{{\n\t\t{field_name} = value;\n\t}}"
            return f"{setter_method}\n{getmet}"
        else:
            return getmet


if __name__ == '__main__':
    input_file = 'input.java'
    getsetadd(input_file)
