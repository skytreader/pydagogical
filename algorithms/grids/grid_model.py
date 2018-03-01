from components.core import GameModel
from components.helpers.grid import BorderProperties, QuadraticGrid

class Grid(GameModel):

    FREE = True
    BLOCKED = False

    def __init__(self, grid_size):
        self.qg = QuadraticGrid(
            grid_size[0], grid_size[1], diag_neighbors=False,
            border_properties=BorderProperties()
        )
        for i in range(width):
            for j in range(height):
                self.qg.grid[i][j] = FREE

    def toggle(self, row, col):
        self.qg.grid[row][col] = not self.qg.grid[row][col]
