# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# HELPER FUNCTIONS AND IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def powerOf(numOne, numTwo):
    return str(float(numOne) ** float(numTwo))


def multiply(numOne, numTwo):
    return str(float(numOne) * float(numTwo))


def divide(numOne, numTwo):
    try:
        return str(float(numOne) / float(numTwo))
    except ZeroDivisionError:
        return "You can't divide by zero!"


def add(numOne, numTwo):
    return str(float(numOne) + float(numTwo))


def subtract(numOne, numTwo):
    return str(float(numOne) - float(numTwo))



def tokenize(operations, equation, lastResult=""):
    num = lastResult
    tokens = []
    for char in equation:
        if char in operations.keys():
            tokens.append(num)
            tokens.append(char)
            num = ""
        elif char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
            num += char
        else:
            continue
    tokens.append(num)
    return tokens



def evaluate(operations, tokensIn):
    tokens = tokensIn
    for operator in operations.keys():
        newTokens = [tokens[0]]
        for idx in range(1, len(tokens), 2):
            op = tokens[idx]
            right = tokens[idx+1]
            if op == operator:
                left = newTokens.pop()
                result = operations[op](left, right)
                newTokens.append(result)
            else:
                newTokens.append(op)
                newTokens.append(right)
        tokens = newTokens
    return tokens.pop()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN FUNCTION DEFINITION
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    appOn = True

    operations = {"^": powerOf,
                  "*": multiply,
                  "/": divide,
                  "+": add,
                  "-": subtract}

    while appOn:
        print("")
        rawEq = input(" --> ")

        if rawEq in ["quit", "exit", "off"]:
            appOn = False
        else:
            eqTokens = tokenize(operations, rawEq)
            result = evaluate(operations, eqTokens)

            print("")
            print(f"{rawEq} = {result}")
            



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MATH FUNCTION CALL
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
main()
