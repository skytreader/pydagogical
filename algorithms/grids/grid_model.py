from components.core import GameModel
from components.helpers.grid import BorderProperties, QuadraticGrid
from screen import GridScreen

class Grid(GameModel):

    FREE = True
    BLOCKED = False

    def __init__(self, grid_size, max_size):
        super(Grid, self).__init__()
        self.qg = QuadraticGrid(
            grid_size[0], grid_size[1], max_size[0], max_size[1],
            diag_neighbors=False, border_properties=BorderProperties()
        )
        for i in range(grid_size[0]):
            for j in range(grid_size[1]):
                self.qg.grid[i][j] = GridScreen.UNTAKEN

    def toggle(self, row, col):
        self.qg.grid[row][col] = not self.qg.grid[row][col]
    
    def render(self, **kwargs):
        row = kwargs["row"]
        col = kwargs["col"]

        if self.qg.grid[row][col]:
            return GridScreen.UNTAKEN
        else:
            return GridScreen.BLOCKED
