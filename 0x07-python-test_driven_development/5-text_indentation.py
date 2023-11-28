#!/usr/bin/python3

"""
This is text_indentation function
Increments two new lines after "?.:"
Doesn't print any spaces at the beginning
or end of the sentences
"""


def text_indentation(text):
    """

    Prints a text with indentation

    Args:
        text (str): The text to prints

    Raises:
        TypeError: If `text` isn't string

    """

    if type(text) is not str:
        raise TypeError('text must be a string')

    length = len(text)
    index = 0
    new_str = ''
    start = True

    while index < length:
        if text[index] == ' ' and start is True:
            index += 1
            continue

        start = False

        if text[index] in '.?:':
            new_str += text[index]
            new_str += '\n'
            new_str += '\n'
            index += 1

            while index < length and text[index] == ' ':
                index += 1

            continue

        if index < length:
            new_str += text[index]
            index += 1

    print(new_str, end='')
