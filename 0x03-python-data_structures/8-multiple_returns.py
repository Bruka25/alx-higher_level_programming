#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)

# if sentence is empty return None
    if not sentence:
        return None

    first = sentence[0]
    return length, first
