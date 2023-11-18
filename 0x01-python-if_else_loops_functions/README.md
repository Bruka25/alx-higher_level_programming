The following programs are for ALX 0x01-python-if_else_loops_functions project, inside it contains the following programs:

* A program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print whether the number stored in the variable number is positive or negative
* A program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable number
* A program that prints the ASCII alphabet, in lowercase, not followed by a new line.
* A program that prints the ASCII alphabet, in lowercase, not followed by a new line. Print all the letters except q and e
* A program that prints all numbers from 0 to 98 in decimal and in hexadecimal
* A program that prints numbers from 0 to 99
* A program that prints all possible different combinations of two digits
* A function that checks for lowercase character
* A function that prints a string in uppercase followed by a new line
* A function that prints the last digit of a number
* A function that adds two integers and returns the result
* A function that computes a to the power of b and return the value
* A function that prints the numbers from 1 to 100 separated by a space
* A function in C that inserts a number into a sorted singly linked list
* A  program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (z in lowercase and Y in uppercase) , not followed by a new line
* A function that creates a copy of the string, removing the character at the position n (not the Python way, the “C array index”)
* A Python function def magic_calculation(a, b, c): that does exactly the same as the following Python bytecode:
```
  3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
```

Python If-Else Functionality Guide
Overview
Welcome to the Python If-Else Functionality Guide! This document provides an introduction and explanation of conditional statements (if, else, elif) in Python, demonstrating their usage and syntax.

* Table of Contents
* Introduction to Conditional Statements
* Basic Syntax
* Multiple Conditions with elif
* Nested if Statements
* Repository Structure
* Usage
* Contributing
* License

Introduction to Conditional Statements
Conditional statements in Python enable the execution of specific code blocks based on the evaluation of conditions. They allow for decision-making within programs by evaluating whether an expression is True or False.

Basic Syntax
if Statement

```
if condition:
    # Code block executed if the condition is True
    statement1
    statement2
    # ...
```

if-else Statement

```
if condition:
    # Code block executed if the condition is True
    statement1
    statement2
    # ...
else:
    # Code block executed if the condition is False
    statementA
    statementB
    # ...
```

Multiple Conditions with elif
The elif statement allows evaluating multiple conditions sequentially after an initial if statement. It checks for another condition if the previous condition(s) are False.

```
if condition1:
    # Code block executed if condition1 is True
    statement1
    statement2
    # ...
elif condition2:
    # Code block executed if condition1 is False and condition2 is True
    statementA
    statementB
    # ...
else:
    # Code block executed if both condition1 and condition2 are False
    statementX
    statementY
    # ...

```
Nested if Statements
if statements can be nested within other if or else blocks to create more complex conditional structures based on multiple conditions.

Repository Structure
README.md: This document providing an overview and explanation of if-else functionality in Python.
example.py: Contains example Python code demonstrating if-else statements.
Usage
Review the example.py file to see practical examples of if-else statements in Python. Execute the code to observe the conditional behavior.

```
python example.py
```

Contributing
Contributions to enhance or expand the documentation on if-else functionality or examples are welcome! Fork this repository, make your changes, and submit a pull request.

License
This repository is licensed under the MIT License, allowing usage, modification, and distribution.

This README.md file aims to provide an introduction to if-else functionality in Python, explaining the syntax and usage of conditional statements. Adjust or expand upon this document to suit the specific needs of your project related to if-else functions in Python.






