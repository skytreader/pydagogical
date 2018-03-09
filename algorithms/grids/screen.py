from components.core import GameScreen
from components.core import Colors

class GridScreen(GameScreen):

    UNTAKEN = Colors.MAX_WHITE
    BLOCKED = Colors.ADVENTURE_DARK

    def __init__(self, config, model):
        super(GridScreen, self).__init__(config, model)

    def draw_screen(self, window):
        self.model.qg.draw(window, self)
