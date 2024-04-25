#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generates Pascal's triangle of size n
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # First element of each row is always 1

        # Calculate the elements in between using the previous row
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)  # Last element of each row is always 1
        triangle.append(new_row)

    return triangle
