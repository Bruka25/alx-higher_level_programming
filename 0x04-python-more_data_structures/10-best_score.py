#!/usr/bin/python3

def best_score(dictionary):
    if dictionary is None or dictionary == {}:
        return None

    best = max(dictionary.values())
    for key, value in dictionary.items():
        if value is best:
            return key
