#!/usr/bin/python3
"""Island perimeter Task
"""


def island_perimeter(grid):
    """Task Sol.
    """
    perimeter = 0
    if type(grid) != list:
        return 0
    n = len(grid)
    for i, row in enumerate(grid):
        l = len(row)
        for j, cell in enumerate(row):
            if cell == 0:
                continue
            land = (
                i == 0 or (len(grid[i - 1]) > j and grid[i - 1][j] == 0),
                j == l - 1 or (l > j + 1 and row[j + 1] == 0),
                i == n - 1 or (len(grid[i + 1]) > j and grid[i + 1][j] == 0),
                j == 0 or row[j - 1] == 0,
            )
            perimeter += sum(land)
    return perimeter
