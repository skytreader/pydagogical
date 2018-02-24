from components.core import GameModel

class Grid(GameModel):

    FREE = True
    BLOCKED = False

    def __init__(self, width, height):
        self.qg = QuadraticGrid(width, height, diag_neighbors=False)
        for i in range(width):
            for j in range(height):
                self.qg.grid[i][j] = FREE

    def toggle(self, row, col):
        self.qg.grid[row][col] = not self.qg.grid[row][col]
