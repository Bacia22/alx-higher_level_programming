#!/usr/bin/python3

def safe_print_integer(value)
""""Print an interger with "{:d}".format().

Args:
    value (int): the integer to print.

    Returns:
    If a TypeError or ValueError occurs - False.
    Otherwise - True.
    """
    Try:
        print("{:d}".format(value))

        return(True)
    except(TypeError, ValueError):
        return(False)
