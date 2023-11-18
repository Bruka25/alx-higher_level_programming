Python Import Modules Guide
Overview
Welcome to the Python Import Modules Guide! This document provides an introduction and explanation of importing modules in Python, demonstrating various ways to import modules, handle namespaces, and utilize imported functionality.

* Table of Contents
* Introduction to Modules
* Importing Modules
* Namespace Handling
* Common Import Patterns
* Repository Structure
* Usage
* Contributing
* License

Introduction to Modules
Modules in Python are files containing Python code that can be imported and used within other Python scripts or modules. They aid in code organization, reusability, and maintainability.

Importing Modules
Basic Import

```
import module_name
```
Import with Alias

```
import module_name as alias
Import Specific Functions/Variables
```

```
from module_name import function_name, variable_name
Import All Functions/Variables
```

```
from module_name import *
```

Namespace Handling
Use the module name or alias to access functions/variables: module_name.function_name() or alias.function_name().
Prevent namespace conflicts by using aliases or importing specific functions/variables.
Common Import Patterns
Standard Library Modules
```
import math
import random
```
Third-Party Modules
```
import requests
import pandas as pd
```
Local Modules
```
import my_custom_module
from my_package import my_submodule
```
Repository Structure
README.md: This document providing an overview and explanation of importing modules in Python.
example.py: Contains example Python code demonstrating various import patterns.
Usage
Clone this repository to your local machine and navigate to the directory:

```
git clone https://github.com/Bruka25/alx-higher_level_programming
cd 0x02-python-import_modules
```
Review the example.py file to see practical examples of importing modules in Python. Execute the code to observe how different import statements work.

```
python example.py
```

Contributing
Contributions to enhance or expand the documentation on importing modules or examples are welcome! Fork this repository, make your changes, and submit a pull request.

License
This repository is licensed under the MIT License, allowing usage, modification, and distribution.

This README.md file aims to provide an introduction to importing modules in Python, explaining various import statements, namespace handling, and common import patterns. Customize or expand upon this document to align with your project's specific needs related to importing modules in Python. Adjust the repository link and directory information accordingly.


The following projects are for ALX 0x02-python-import_modules project inside the alx higher programming language curriculum, inside it contains the following programs:

* A program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3
* A program that imports functions from the file calculator_1.py, does some Maths, and prints the result
* A program that prints the number of and the list of its arguments
* A program that prints the result of the addition of all arguments
* A program that prints all the names defined by the compiled module hidden_4.pyc (please download it locally)
* A program that imports the variable a from the file variable_load_5.py and prints its value
* A program that imports all functions from the file calculator_1.py and handles basic operations
* A program that prints #pythoniscool, followed by a new line, in the standard output
* A Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:
```
 3           0 LOAD_CONST               1 (0)
              3 LOAD_CONST               2 (('add', 'sub'))
              6 IMPORT_NAME              0 (magic_calculation_102)
              9 IMPORT_FROM              1 (add)
             12 STORE_FAST               2 (add)
             15 IMPORT_FROM              2 (sub)
             18 STORE_FAST               3 (sub)
             21 POP_TOP

  4          22 LOAD_FAST                0 (a)
             25 LOAD_FAST                1 (b)
             28 COMPARE_OP               0 (<)
             31 POP_JUMP_IF_FALSE       94

  5          34 LOAD_FAST                2 (add)
             37 LOAD_FAST                0 (a)
             40 LOAD_FAST                1 (b)
             43 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             46 STORE_FAST               4 (c)

  6          49 SETUP_LOOP              38 (to 90)
             52 LOAD_GLOBAL              3 (range)
             55 LOAD_CONST               3 (4)
             58 LOAD_CONST               4 (6)
             61 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             64 GET_ITER
        >>   65 FOR_ITER                21 (to 89)
             68 STORE_FAST               5 (i)

  7          71 LOAD_FAST                2 (add)
             74 LOAD_FAST                4 (c)
             77 LOAD_FAST                5 (i)
             80 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             83 STORE_FAST               4 (c)
             86 JUMP_ABSOLUTE           65
        >>   89 POP_BLOCK

  8     >>   90 LOAD_FAST                4 (c)
             93 RETURN_VALUE

 10     >>   94 LOAD_FAST                3 (sub)
             97 LOAD_FAST                0 (a)
            100 LOAD_FAST                1 (b)
            103 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
            106 RETURN_VALUE
            107 LOAD_CONST               0 (None)
            110 RETURN_VALUE
```
* A program that prints the alphabet in uppercase, followed by a new line


