#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    add=[]

    for i in range(2):
        # if a tuple has a value use otherwise make it 0
        value_a = tuple_a[i] if i < len(tuple_a) else 0
        value_b = tuple_b[i] if i < len(tuple_b) else 0

        add.append(value_a + value_b)

    output = tuple(add)
    return output 
