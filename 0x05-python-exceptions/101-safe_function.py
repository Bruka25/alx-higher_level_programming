#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    try:
        output = fct(*args)
    except Exception as err:
        output = None
        print("Exception: {}".format(err), file=sys.stderr)
    finally:
        return output
