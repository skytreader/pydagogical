import unittest

"""
Grid-traversal-related snippets.

Assumptions:

* Zero-based indexing.
* When limits are asked for, the value given is 1 more than the last addressable
  value for that dimension in the grid.

Common variations:

* You might need to keep track of cells already visited and exclude them from
  being considered as adjacent cells.
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
            if (r, c) != p:
                adjacent.append((r, c))
    
    return adjacent

def get_adjacent_4c(p, row_limit, col_limit):
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
    adjacent.extend([(r, p[1]) for r in rows])
    adjacent.extend([(p[0], c) for c in cols])

    return adjacent

class FunctionsTest(unittest.TestCase):
    
    def test_get_adjacent_8c(self):
        full_neighbors = set([(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0),
          (2, 1), (2, 2)])
        self.assertEqual(full_neighbors, set(get_adjacent_8c((1, 1), 4, 4)))

        up_left_neighbors = set([(0, 1), (1, 0), (1, 1)])
        self.assertEqual(up_left_neighbors, set(get_adjacent_8c((0, 0), 4, 4)))

        down_left_neighbors = set([(2, 0), (2, 1), (3, 1)])
        self.assertEqual(down_left_neighbors, set(get_adjacent_8c((3, 0), 4, 4)))

        down_right_neighbors = set([(3, 2), (2, 2), (2, 3)])
        self.assertEqual(down_right_neighbors, set(get_adjacent_8c((3, 3), 4, 4)))

        up_right_neighbors = set([(0, 2), (1, 2), (1, 3)])
        self.assertEqual(up_right_neighbors, set(get_adjacent_8c((0, 3), 4, 4)))

    def test_get_adjacent_4c(self):
        full_neighbors = set([(0, 1), (1, 0), (1, 2), (2, 1)])
        self.assertEqual(full_neighbors, set(get_adjacent_4c((1, 1), 4, 4)))

if __name__ == "__main__":
    unittest.main()
