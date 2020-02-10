class converter():
    csharp_code = []
    python_code = []
    datatypes = ['int', 'float', 'string', 'char']
    cs_to_py_btn = {
        "Console.WriteLine": "print",
        "Console.Write": "print",
        "Console.Read": "input",
        "Console.ReadLine": "input"
    }


    def convert_to_python(code_comp, code_syntax):
        no_of_indents = 0
        for i in code_comp:
            try:
                i.remove(";")
            except:
                pass
            for n, a in enumerate(i):
                for j in converter.cs_to_py_btn:
                    if a == j:
                        i[n] = converter.cs_to_py_btn[j]
            try:
                i.remove("}")
                no_of_indents -= 1
            except:
                pass
            for j in converter.datatypes:
                try:
                    i.remove(j)
                except:
                    pass
            try:
                if i[0] == "else" and i[1] == "if":
                    i[0] = "elif"
                    del i[1]
            except:
                pass
            for n in range(no_of_indents):
                i.insert(0, "\t")
            for n, val in enumerate(i):
                if val == "{":
                    no_of_indents += 1
                    i[n] = ":"

            converter.python_code.append(i)

        print("Python code:")
        for i in converter.python_code:
            print(' '.join(i))
