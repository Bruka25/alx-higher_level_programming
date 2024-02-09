0x05 Python Exceptions
Welcome to the "0x05-python-exceptions" repository! This repository contains code related to Python exceptions, aimed athelping developers understand how to handle errors and exceptions effectively in Python programming.

Table of Contents

Introduction

Installation

Usage

Contributing

License

Introduction

In Python programming, exceptions are events that occur during the execution of a program that disrupt the normal flow of the program's instructions. Properly handling exceptions is crucial for writing robust and reliable software. This repository provides examples and exercises related to Python exceptions to help developers become proficient in handling errors gracefully.

Installation

To use the code in this repository, follow these steps:

1. Clone the repository to your local machine:

```
git clone https://github.com/Bruka25/alx-higher_level_programming
```
2. Navigate to the repository directory:

```
cd 0x05-python-exceptions
```
3. You're ready to explore the code related to Python exceptions!

Usage

This repository contains Python scripts, each representing a specific question related to Python exceptions along with its corresponding solution. To make use of the repository:

1. Navigate to the directory containing the Python scripts:

```
cd 0x05-python-exceptions
```
2. Explore the Python scripts available in the repository. Each Python script is named descriptively to indicate the question it addresses

3. Open a Python script file to view both the question and its solution within the same file. The script typically consists of the following sections:

           -> Description of the problem or question.
           -> Python code implementing the solution to the problem.

4. Study the provided Python code to understand the problem and solution approach.

5. Modify the code as needed, experiment with different solutions, and test them to deepen your understanding of Python exceptions.

6. Feel free to use the provided code snippets in your own projects or learning exercises, ensuring to understand how and why they work.

Contributing

Contributions to this repository are welcome! If you have ideas for improving existing code, adding new examples, or fixing issues, please feel free to submit a pull request. Before contributing, please review the contribution guidelines.

License

This repository is licensed under the MIT License. See the LICENSE file for details.


The following projects are for ALX 0x05-python-exceptions for the alx higher level programming curriculum, inside it contains the following python files:

* A function that prints x elements of a list
* A function that prints an integer with "{:d}".format()
* A function that prints the first x elements of a list and only integers
* A function that divides 2 integers and prints the result
* A function that divides element by element 2 lists
* A function that raises a type exception
* A function that raises a name exception with a message
* A function that prints an integer
* A function that executes a function safely
* Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:

```
3           0 LOAD_CONST               1 (0)
              3 STORE_FAST               2 (result)

  4           6 SETUP_LOOP              94 (to 103)
              9 LOAD_GLOBAL              0 (range)
             12 LOAD_CONST               2 (1)
             15 LOAD_CONST               3 (3)
             18 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             21 GET_ITER
        >>   22 FOR_ITER                77 (to 102)
             25 STORE_FAST               3 (i)

  5          28 SETUP_EXCEPT            49 (to 80)

  6          31 LOAD_FAST                3 (i)
             34 LOAD_FAST                0 (a)
             37 COMPARE_OP               4 (>)
             40 POP_JUMP_IF_FALSE       58

  7          43 LOAD_GLOBAL              1 (Exception)
             46 LOAD_CONST               4 ('Too far')
             49 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             52 RAISE_VARARGS            1
             55 JUMP_FORWARD            18 (to 76)

  9     >>   58 LOAD_FAST                2 (result)
             61 LOAD_FAST                0 (a)
             64 LOAD_FAST                1 (b)
             67 BINARY_POWER
             68 LOAD_FAST                3 (i)
             71 BINARY_TRUE_DIVIDE
             72 INPLACE_ADD
             73 STORE_FAST               2 (result)
        >>   76 POP_BLOCK
             77 JUMP_ABSOLUTE           22

 10     >>   80 POP_TOP
             81 POP_TOP
             82 POP_TOP

 11          83 LOAD_FAST                1 (b)
             86 LOAD_FAST                0 (a)
             89 BINARY_ADD
             90 STORE_FAST               2 (result)

 12          93 BREAK_LOOP
             94 POP_EXCEPT
             95 JUMP_ABSOLUTE           22
             98 END_FINALLY
             99 JUMP_ABSOLUTE           22
        >>  102 POP_BLOCK

 13     >>  103 LOAD_FAST                2 (result)
            106 RETURN_VALUE

```
* Three C functions that print some basic info about Python lists, Python bytes an Python float objects
