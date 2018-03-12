from components.core import GameConfig, GameLoop
from grid_model import Grid
from screen import GridLoopEvents, GridScreen

if __name__ == "__main__":
    config = GameConfig(window_size=(600, 600), debug_mode=True, log_to_terminal=True)
    model = Grid((10, 10))
    screen = GridScreen(config, model)
    loop_events = GridLoopEvents(screen)
    loop = GameLoop(loop_events)
    loop.go()
