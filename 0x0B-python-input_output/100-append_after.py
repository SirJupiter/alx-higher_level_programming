#!/usr/bin/python3
"""Module contains 'append_after' function"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text into a file after each line
    containing a specific string.

    Args:
        filename (str): Name of the file.
        search_string (str): String to search for in each line.
        new_string (str): String to insert after each line
        containing the search string.
    """
    # Open the file for reading and writing using the 'with' statement
    with open(filename, 'r+') as file:
        # Read the lines of the file into a list
        lines = file.readlines()

        # Iterate through the lines of the file
        for i, line in enumerate(lines):
            # If the search string is found in the line
            if search_string in line:
                # Insert the new string after this line
                lines.insert(i + 1, new_string + '\n')

        # Move the file cursor to the beginning of the file
        file.seek(0)

        # Write the modified lines back to the file
        file.writelines(lines)
