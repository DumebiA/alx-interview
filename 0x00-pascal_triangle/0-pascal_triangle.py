#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """Generates Pascal's triangle of size n
    """
    triangle = []
    if n > 0:
        for i in range(1, n + 1):
            newLevel = []
            D = 1
            for j in range(1, i + 1):
                newLevel.append(D)
                D = D * (i - j) // j
            triangle.append(newLevel)
    return triangle
