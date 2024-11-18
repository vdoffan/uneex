import re

def calculator():
    variables = {}

    while True:
        line = input().strip()
        if line == "":
            break
        if line.startswith("#"):
            continue
        if "=" in line:
            left, right = line.split("=", 1)
            left = left.strip()
            right = right.strip()
            if not left.isidentifier():
                print("Assignment error")
                continue
            try:
                if ':=' not in right:
                    compile(right, "<string>", "eval")
                    undefined_vars = [
                        var for var in re.findall(r'\b[A-Za-z_][A-Za-z0-9_]*\b', right)
                        if var not in variables and var not in {"True", "False", "None"}
                    ]
                    if undefined_vars:
                        print("Name error")
                        continue
                value = eval(right, {"__builtins__": None}, variables)
                variables[left] = value
            except SyntaxError:
                print("Syntax error")
            except Exception:
                print("Runtime error")
        else:
            try:
                if '.' not in line:
                    compile(line, "<string>", "eval")
                    undefined_vars = [
                        var for var in re.findall(r'\b[A-Za-z_][A-Za-z0-9_]*\b', line)
                        if var not in variables and var not in {"True", "False", "None"}
                    ]
                    if undefined_vars:
                        print("Name error")
                        continue
                result = eval(line, {"__builtins__": None}, variables)
                print(result)
            except SyntaxError:
                print("Syntax error")
            except Exception:
                print("Runtime error")

calculator()