0x09 Python Everything Is Object
Welcome to the "0x09-python-everything_is_object" repository! This repository delves into the concept of objects in Python, exploring how everything in Python is an object and understanding the implications of this object-oriented paradigm.

Table of Contents

Introduction
Installation
Usage
Contributing
License

Introduction
In Python, everything is an object. This means that every variable, function, and data structure in Python is an object with its own attributes and methods. Understanding this fundamental concept is crucial for writing Python code effectively and leveraging the full power of the language's object-oriented features. This repository provides examples and explanations to help developers grasp the concept of objects in Python and how they impact programming in the language.

Installation
To use the code in this repository, follow these steps:

1. Clone the repository to your local machine:

```
git clone https://github.com/Bruka25/alx-higher_level_programming
```
2. Navigate to the repository directory:

```
cd 0x09-python-everything_is_object
```
3. You're ready to explore the code related to objects in Python!

Usage
This repository contains Python scripts and examples, each focusing on different aspects of objects in Python. To make use of the repository:

1. Navigate to the directory containing the Python scripts:

```
cd 0x09-python-everything_is_object
```
2. Explore the Python scripts available in the repository. Each script demonstrates a specific concept related to objects in Python.

3. Open a Python script file to view the implementation and explanation of the concept.

4. Study the provided Python code and accompanying explanations to understand the concept and its implications.

5. Experiment with the code, modify it as needed, and test different scenarios to deepen your understanding of objects in Python.

5. Feel free to use the provided code snippets and examples as references for working with objects in your own Python projects.

Contributing
Contributions to this repository are welcome! If you have ideas for improving existing code, adding new examples, or fixing issues, please feel free to submit a pull request. Before contributing, please review the contribution guidelines.

License
This repository is licensed under the MIT License. See the LICENSE file for details.


The following project is called 0x09-python-everything_is_object, and it's for ALX high level programming curriculum, inside it conntains the following python scripts and text files:

* The function used to get the type of an object
* The fuction to get the variable identifier
* The answer to the following code, do a and b point to the same object? Answer with Yes or No
```
>>> a = 89
>>> b = 100
```
* The answer to the following code, do a and b point to the same object? Answer with Yes or No
```
>>> a = 89
>>> b = 89
```

* The answer to the following code, do a and b point to the same object? Answer with Yes or No
```
>>> a = 89
>>> b = a
```
* The answer to the following code, do a and b point to the same object? Answer with Yes or No
```
>>> a = 89
>>> b = a + 1
```
* The answer to What do these 3 lines print
```
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```
* The answer to What do these 3 lines print
```
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```
* The answer to What do these 3 lines print
```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```
* The answer to What do these 3 lines print
```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
```
* The answer to What do these 3 lines print
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```
* The answer to What do these 3 lines print
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
```
* The answer to What do these 3 lines print
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```
* The answer to What do these 3 lines print
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```
*  The answer to What does this script print
```
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```
* The answer to What does this script print
```
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```
* The answer to What does this script print
```
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```
* The answer to What does this script print 
```
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```
* The answer to What does this script print
```
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1
```
* A function def copy_list(l): that returns a copy of a list
* The answer to Is a a tuple? Answer with Yes or No
```
a = ()
```
* The answer to Is a a tuple? Answer with Yes or No
```
a = (1, 2)
```
* The answer to Is a a tuple? Answer with Yes or No
```
a = (1)
```
* The answer to Is a a tuple? Answer with Yes or No
```
a = (1, )
```
* The answer to Is a a tuple? Answer with Yes or No
```
a = (1)
b = (1)
a is b
```
* The answer to What does this script print
```
a = (1, 2)
b = (1, 2)
a is b
```
* The answer to What does this script print
```
a = ()
b = ()
a is b
```
* The answer to Will the last line of this script print 139926795932424? Answer with Yes or No
```
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```
* The answer to Will the last line of this script print 139926795932424? Answer with Yes or No
```
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```
* A function magic_string() that returns a string “BestSchool” n times the number of the iteration
* A  class LockedClass with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name

* Assuming we are using a CPython implementation of Python3 with default options/configuration:

         How many int objects are created by the execution of the first line of the script? (103-line1.txt)
         How many int objects are created by the execution of the second line of the script (103-line2.txt)
```
a = 1
b = 1
```
* Assuming we are using a CPython implementation of Python3 with default options/configuration:

         How many int objects are created by the execution of the first line of the script? (104-line1.txt)
         How many int objects are created by the execution of the second line of the script (104-line2.txt)
         After the execution of line 3, is the int object pointed by a deleted? Answer with Yes or No (104-line3.txt)
         After the execution of line 4, is the int object pointed by b deleted? Answer with Yes or No (104-line4.txt)
         How many int objects are created by the execution of the last line of the script (104-line5.txt)
```
a = 1024
b = 1024
del a
del b
c = 1024
```
* Assuming we are using a CPython implementation of Python3 with default options/configuration:

         Before the execution of line 2 (print("Love")), how many int objects have been created and are still in memory? (105-line1.txt)
```
print("I")
print("Love")
print("Python"
```
* Assuming we are using a CPython implementation of Python3 with default options/configuration (For answers with numbers use integers, don’t spell out the word):

         How many string objects are created by the execution of the first line of the script? (106-line1.txt)
         How many string objects are created by the execution of the second line of the script (106-line2.txt)
         After the execution of line 3, is the string object pointed by a deleted? Answer with Yes or No (106-line3.txt)
         After the execution of line 4, is the string object pointed by b deleted? Answer with Yes or No (106-line4.txt)
         How many string objects are created by the execution of the last line of the script (106-line5.txt)
```
a = "SCHL"
b = "SCHL"
del a
del b
c = "SCHL"
```




























































