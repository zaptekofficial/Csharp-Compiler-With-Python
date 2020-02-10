def dict(userInput):
    builtin_func = [
        "Console.WriteLine",
        "Console.Write",
        "Console.Read",
        "Console.ReadLine"
    ]
    symbols = {
        ";": "term",
        "{": "cbr-op",
        "}": "cbr-cl",
        "(": "rbr-op",
        ")": "rbr-cl"
    }
    keywords = {
        "while": "loop-wh",
        "for": "loop-for",
        "if": "cond-if",
        "else": "cond-el",
    }
    dataTypes = {
        "int": "dt-int",
        "float": "dt-fl",
        "char": "dt-ch",
        "string": "dt-str",
        "class": "dt-cl"
    }
    operators = [
        "+",
        "=",
        "-",
        "/",
        "*",
        ">",
        "<",
        "++",
        "--",
        "==",
        "!",
        "!=",
        ">=",
        "<=",
        "!",
        "!=",
        "%",
        "||",
        "&&",
        "+=",
        "-=",
        "*=",
        "/="
    ]
    isFound = False
    for i in builtin_func:
        if i == userInput:
            print(userInput + " is a built-in function")
            return "btf"
    for i in keywords:
        if i == userInput:
            print("The keyword is " + i)
            return keywords[i]
    for i in symbols:
        if i == userInput:
            print("The symbol is " + i)
            return symbols[i]
    for i in dataTypes:
        if i == userInput:
            print("The data type is " + i)
            return dataTypes[i]

    if isFound is False:
        for i in operators:
            if userInput == i:
                print("The operator is " + i)
                return "op"

    if isFound is False:
        if userInput.startswith("\"") and userInput.endswith("\""):
            print("The input is string")
            return "val-str"
        if isFound is False and userInput.startswith("\'") and userInput.endswith("\'") and len(userInput) == 3:
            for i in range(65, 122):
                if ord(userInput[1]) == i:
                    print("The input is character")
                    return "val-ch"
        if isFound is False and userInput.__contains__("."):
            tempString = userInput.replace(".", "")
            tempVar = 0
            for i in tempString:
                for j in range(48, 57):
                    if ord(i) == j:
                        tempVar += 1
            if tempVar == len(tempString):
                print("The input is float")
                return "val-fl"
        if isFound is False and userInput.isdigit():
            tempVar = 0
            for i in userInput:
                for j in range(48, 57):
                    if ord(i) == j:
                        tempVar += 1
            if tempVar == len(userInput):
                print("The input is int")
                return "val-int"
        if isFound is False:
            print(userInput + " is an identifier")
            return "identifier"

