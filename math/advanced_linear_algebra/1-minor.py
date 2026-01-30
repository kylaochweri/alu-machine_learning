#!/usr/bin/env python3
"""
This module contains a function to calculate the minor matrix of a matrix.
"""


def determinant(matrix):
    """Helper function to calculate the determinant of a matrix."""
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        if matrix == [[]]:
            return 1
        raise ValueError("matrix must be a square matrix")

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return (matrix[0][0] * matrix[1][1] -
                matrix[0][1] * matrix[1][0])

    det = 0
    for col in range(n):
        minor = [
            row[:col] + row[col + 1:]
            for row in matrix[1:]
        ]
        det += ((-1) ** col) * matrix[0][col] * determinant(minor)
    return det


def minor(matrix):
    """Calculates the minor matrix of a matrix.

    Args:
        matrix (list of lists): A non-empty square matrix.

    Returns:
        list of lists: The minor matrix.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is not a non-empty square matrix.
    """
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    if n == 1:
        return [[1]]

    minor_matrix = []
    for i in range(n):
        row_minors = []
        for j in range(n):
            # Exclude row i and column j
            sub_matrix = [
                row[:j] + row[j + 1:]
                for k, row in enumerate(matrix)
                if k != i
            ]
            row_minors.append(determinant(sub_matrix))
        minor_matrix.append(row_minors)

    return minor_matrix
