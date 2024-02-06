#!/usr/bin/python3
"""Module contains 'write_file' function"""


def write_file(filename="", text=""):
    """Function writes a string to a text file

    Args:
        filename (file): name of file to be opened
        text (str): string to be written in the file

    Returns:
        char_written (int): numbers of characters written
    """

    with open(filename, "w", encoding="utf-8") as file:
        char_written = file.write(text)
        return char_written
