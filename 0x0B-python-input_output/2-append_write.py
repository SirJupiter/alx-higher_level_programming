#!/usr/bin/python3
"""Module contains 'append_write' function"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file

    Args:
        filename (file): file to which text will be appended
        text (str): string to append to file

    Returns:
        char_appended (int): number of characters added

    """

    with open(filename, 'a+', encoding="utf-8") as file:
        char_appended = file.write(text)
        return char_appended
