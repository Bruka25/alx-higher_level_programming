#!/usr/bin/python3

"""Script that reads input from stdin and
   counts the occurance of HTTP status
   code and calculates the total size
   of a file
"""
import sys


def status_print():
    """Functionprints the size and the count
       of HTTP status code
       Raises error when there is keyboard
       inturruption
    """
    print('File size: {:d}'.format(byte))

    for status_code, code_occur in sorted(stat_codes.items()):
        if code_occur > 0:
            print('{}: {:d}'.format(status_code, code_occur))


stat_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

counter = 0
byte = 0

try:

    for line in sys.stdin:
        if counter != 0 and counter % 10 == 0:
            status_print()

        white_spl = line.split()

        try:

            status_code = int(white_spl[-2])

            if str(status_code) in stat_codes.keys():
                stat_codes[str(status_code)] += 1
        except (IndexError, ValueError):
            pass

        try:
            byte += int(white_spl[-1])
        except (IndexError, ValueError):
            pass

        counter += 1

    status_print()
except KeyboardInterrupt:
    status_print()
    raise
