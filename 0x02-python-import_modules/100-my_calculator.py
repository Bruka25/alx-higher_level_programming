#!/usr/bin/python3

if __name__ == "__main__":
    """
    import the argv list and all the necessary
    functions from the calculator_1 module
    """
    from sys import argv
    from calculator_1 import add, sub, mul, div

    if len(argv) != 4:
        print("Usage:", argv[0], "<a> <operator> <b>")
        exit(1)

# operate the calculation when a given sign is invoked

    a, sign, b = int(argv[1]), argv[2], int(argv[3])
    operators = {'+': add, '-': sub, '*': mul, '/': div}
    if sign not in operators:
        print("Unknown operator. Only: +, -, * and / available")
        exit(1)
    print('{:d} {} {:d} = {:d}'.format(a, sign, b, operators[sign](a, b)))
