class syntacticAnalyzer():
    num_of_opcbr = 0
    num_of_clcbr = 0
    num_of_oprbr = 0
    num_of_clrbr = 0
    has_error = False
    std_syntax = [
        # for int datatype
        ['dt-int', 'identifier', 'op', 'val-int', 'term'],
        ['dt-int', 'identifier', 'op', 'identifier', 'term'],
        ['dt-int', 'identifier', 'op', 'val-int', 'op', 'val-int', 'term'],
        ['dt-int', 'identifier', 'op', 'identifier', 'op', 'val-int', 'term'],
        ['dt-int', 'identifier', 'op', 'identifier', 'op', 'identifier', 'term'],
        # for float datatype
        ['dt-fl', 'identifier', 'op', 'val-fl', 'term'],
        ['dt-fl', 'identifier', 'op', 'val-fl', 'op', 'val-fl', 'term'],
        ['dt-fl', 'identifier', 'op', 'identifier', 'term'],
        ['dt-fl', 'identifier', 'op', 'identifier', 'op', 'val-fl', 'term'],
        ['dt-fl', 'identifier', 'op', 'identifier', 'op', 'identifier', 'term'],
        # for char datatype
        ['dt-ch', 'identifier', 'op', 'val-ch', 'term'],
        ['dt-ch', 'identifier', 'op', 'identifier', 'term'],
        # for string datatype
        ['dt-str', 'identifier', 'op', 'val-str', 'term'],
        ['dt-str', 'identifier', 'op', 'identifier', 'op', 'val-str', 'term'],
        ['dt-str', 'identifier', 'op', 'identifier', 'op', 'identifier', 'term'],
        ['dt-str', 'identifier', 'op', 'identifier', 'op', 'identifier', 'op', 'identifier', 'term'],
        # generalized
        ['cbr-op'],
        ['cbr-cl'],
        ['identifier', 'op', 'identifier', 'term'],
        ['identifier', 'op', 'identifier', 'op', 'identifier', 'op', 'identifier', 'term'],
        ['identifier', 'op', 'identifier', 'op', 'identifier', 'term'],
        ['identifier', 'op', 'val-int', 'term'],
        ['identifier', 'op', 'val-fl', 'term'],
        ['identifier', 'op', 'val-ch', 'term'],
        ['identifier', 'op', 'val-str', 'term'],
        # for while loop
        ['dt-int', 'identifier', 'op', 'btf', 'rbr-op', 'rbr-cl', 'term'],
        ['loop-wh', 'rbr-op', 'identifier', 'op', 'identifier', 'rbr-cl'],
        ['loop-wh', 'rbr-op', 'identifier', 'op', 'identifier', 'rbr-cl', 'cbr-op'],
        ['loop-wh', 'rbr-op', 'identifier', 'op', 'val-int', 'rbr-cl', 'cbr-op'],
        ['loop-wh', 'rbr-op', 'identifier', 'op', 'val-str', 'rbr-cl', 'cbr-op'],
        ['loop-wh', 'rbr-op', 'identifier', 'op', 'val-ch', 'rbr-cl', 'cbr-op'],
        ['loop-wh', 'rbr-op', 'identifier', 'op', 'val-fl', 'rbr-cl', 'cbr-op'],
        ['identifier', 'op', 'btf', 'rbr-op', 'rbr-cl', 'term'],
        # for 'for' loop == REMAINING
        ['loop-for', 'rbr-op', 'dt-int', 'identifier', 'op', 'val-int', 'term', 'identifier', 'op', 'val-int', 'term',
         'identifier', 'op', 'rbr-cl', 'cbr-op'],
        ['loop-for', 'rbr-op', 'identifier', 'op', 'val-int', 'term', 'identifier', 'op', 'val-int', 'term', 'identifier', 'op', 'rbr-cl', 'cbr-op'],
        ['loop-for', 'rbr-op', 'dt-int', 'identifier', 'op', 'identifier', 'term', 'identifier', 'op', 'val-int', 'term', 'identifier', 'op', 'rbr-cl', 'cbr-op'],
        ['loop-for', 'rbr-op', 'dt-int', 'identifier', 'op', 'val-int', 'term', 'identifier', 'op', 'identifier', 'term', 'identifier', 'op', 'rbr-cl', 'cbr-op'],
        # for built-in functions
        ['btf', 'rbr-op', 'val-str', 'rbr-cl', 'term'],
        ['btf', 'rbr-op', 'identifier', 'rbr-cl', 'term'],
        ['identifier', 'op', 'btf', 'identifier', 'term'],
        ['identifier', 'op', 'btf', 'rbr-op', 'val-str', 'rbr-cl', 'term'],
        # for if condition
        ['cond-if', 'rbr-op', 'identifier', 'op', 'identifier', 'rbr-cl'],
        ['cond-if', 'rbr-op', 'identifier', 'op', 'identifier', 'rbr-cl', 'cbr-op'],
        ['cond-if', 'rbr-op', 'identifier', 'op', 'val-int', 'rbr-cl', 'cbr-op'],
        ['cond-if', 'rbr-op', 'identifier', 'op', 'val-str', 'rbr-cl', 'cbr-op'],
        ['cond-if', 'rbr-op', 'identifier', 'op', 'val-ch', 'rbr-cl', 'cbr-op'],
        ['cond-if', 'rbr-op', 'identifier', 'op', 'val-fl', 'rbr-cl', 'cbr-op'],
        # for else if condition
        ['cond-el', 'cond-if', 'rbr-op', 'identifier', 'op', 'identifier', 'rbr-cl'],
        ['cond-el', 'cond-if', 'rbr-op', 'identifier', 'op', 'identifier', 'rbr-cl', 'cbr-op'],
        ['cond-el', 'cond-if', 'rbr-op', 'identifier', 'op', 'val-int', 'rbr-cl', 'cbr-op'],
        ['cond-el', 'cond-if', 'rbr-op', 'identifier', 'op', 'val-str', 'rbr-cl', 'cbr-op'],
        ['cond-el', 'cond-if', 'rbr-op', 'identifier', 'op', 'val-ch', 'rbr-cl', 'cbr-op'],
        ['cond-el', 'cond-if', 'rbr-op', 'identifier', 'op', 'val-fl', 'rbr-cl', 'cbr-op'],
        # for else condition
        ['cond-el'],
        ['cond-el', 'cbr-op']
    ]

    def syntax_check(syntax):
        for i in syntax:
            if "cbr-op" in i:
                syntacticAnalyzer.num_of_opcbr += 1
            if "cbr-cl" in i:
                syntacticAnalyzer.num_of_clcbr += 1
            if "rbr-op" in i:
                syntacticAnalyzer.num_of_oprbr += 1
            if "rbr-cl" in i:
                syntacticAnalyzer.num_of_clrbr += 1

        for n, i in enumerate(syntax):
            is_found = False
            for j in syntacticAnalyzer.std_syntax:
                if i == j:
                    is_found = True
                    break
            if is_found is False:
                print("error in line", n + 1)
                syntacticAnalyzer.has_error = True
        if syntacticAnalyzer.num_of_clcbr != syntacticAnalyzer.num_of_opcbr:
            print("There is a missing curly bracket")
            is_found = True
        if syntacticAnalyzer.num_of_clrbr != syntacticAnalyzer.num_of_oprbr:
            print("There is a missing round bracket")
            is_found = True
        if syntacticAnalyzer.has_error is False:
            print("The code has been successfully compiled and there are no errors")

