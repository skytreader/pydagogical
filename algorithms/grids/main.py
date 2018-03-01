from components.core import GameConfig, GameLoopEvents, GameLoop
from grid_model import Grid
from screen import GridScreen

if __name__ == "__main__":
    config = GameConfig()
    model = Grid((10, 10))
    screen = GridScreen(config, model)
    loop_events = GameLoopEvents(config, screen)
    loop = GameLoop(loop_events)
    loop.go()
