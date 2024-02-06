#!/usr/bin/python3
"""Module contains 'read_file' function"""


def read_file(filename=""):
    """Function reads a text file and prints it to stdout

    Args:
        filename (file): name of file to be opened
    """

    with open(filename, 'r', encoding="utf-8") as file:
        for lines in file:
            print(lines.strip())
