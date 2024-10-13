#!/usr/bin/python3

"""
Islnad Problem
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of an island based on a 2D grid.

    Args:
        grid(list of list of int): 1 rep land and 0 rep water

    Returns:
         int: The total perimeter of the island in the grid.

    """

    'initialize the perimeter counter'
    perimeter = 0

    'interate through each row in the grid'
    for i in range(len(grid)):
        'iterate through each cell in the current row'
        for j in range(len(grid[0])):
            'get the current cell'
            current_cell = grid[i][j]

            'if current cell is 0 skit to next cell'
            if not current_cell:
                continue

            'Check cell above the current one (if it exists)'
            upper_cell = None if not i else grid[i - 1][j]

            'Check cell left of the current one (if it exists)'
            left_cell = None if not j else grid[i][j - 1]

            'Each land cell starts with a perimeter of 4'
            cell_perimeter = 4

            ' If there is land above the current cell subtract 2'
            if upper_cell:
                cell_perimeter -= 2

            'If there is land to the left of the current cell subtract 2'
            if left_cell:
                cell_perimeter -= 2

            'Add the calculated perimeter for the current cell'
            perimeter += cell_perimeter

    return perimeter