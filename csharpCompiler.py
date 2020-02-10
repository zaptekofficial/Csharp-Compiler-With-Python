import lexicalAnalyzer
import syntacticalAnalyzer
import converter

global code_comp
code_comp = []
global code_syntax
code_syntax = []

def compile_code(code):
    code_lines = code.split("\n")
    for i in code_lines:
        code_comp.append(i.split())
    del code_comp[-1]
    print("LEXICAL ANALYSIS:")
    for i in code_comp:
        test_list = []
        for j in i:
            test_list.append(lexicalAnalyzer.dict(j))
        code_syntax.append(test_list)

    print("SYNTACTICAL ANALYSIS:")

    for i in code_syntax:
        print(i)

    syntacticalAnalyzer.syntacticAnalyzer.syntax_check(code_syntax)


code = input("enter code:\n")
while (code[-7:] != "compile") and (code[-7:] != "convert"):
    code += "\n" + input()

if code[-7:] == "compile":
    compile_code(code)

if code[-7:] == "convert":
    compile_code(code)
    converter.converter.convert_to_python(code_comp, code_syntax)

