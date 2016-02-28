"""
Grid-traversal-related snippets.

Assumptions:

* Zero-based indexing.
* When limits are asked for, the value given is 1 more than the last addressable
  value for that dimension in the grid.
"""

def get_adjacent_8c(p, row_limit, col_limit):
    """
    Get the adjacent cells of the given point p assuming adjacency is 8-connected.
    """
    rows = [p[0]]
    cols = [p[1]]

    if p[0] == 0:
        rows.append(p[0] + 1)
    elif p[0] == (row_limit - 1):
        rows.append(p[0] - 1)
    else:
        rows.extend([p[0] + 1, p[0] - 1])

    if p[1] == 0:
        cols.append(p[1] + 1)
    elif p[1] == (col_limit - 1):
        cols.append(p[1] - 1)
    else:
        cols.extend([p[1] + 1, p[1] - 1])

    adjacent = []

    for r in rows:
        for c in cols:
            adjacent.append((r, c))

def get_adjacent_4c(p, row_limit, col_limi):
    """
    Get the adjacent cells of the given point p assuming adjacency is 8-connected.
    """
    rows = []
    cols = []

    if p[0] == 0:
        rows.append(p[0] + 1)
    elif p[0] == (row_limit - 1):
        rows.append(p[0] - 1)
    else:
        rows.extend([p[0] + 1, p[0] - 1])

    if p[1] == 0:
        cols.append(p[1] + 1)
    elif p[1] == (col_limit - 1):
        cols.append(p[1] - 1)
    else:
        cols.extend([p[1] + 1, p[1] - 1])

    adjacent = []

    for r in rows:
        adjacent.append((r, p[1]))

    for c in cols:
        adjacent.append((p[0], c))
