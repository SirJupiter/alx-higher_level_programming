#!/usr/bin/python3
"""Module contains 'pascal_triangle' function"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to row n.

    Args:
        n (int): Number of rows in the triangle.

    Returns:
        list: List of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # First element of each row is always 1
        if i > 0:
            prev_row = triangle[-1]
            for j in range(1, i):  # Calculate intermediate elements of the row
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle
