#!/usr/bin/python3
"""write_file module.

Contains a function that writes a text file.
"""



def write file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the numebr of characters written.
    """
    with open(filename, 'w') as f:
        return f.write(text)
