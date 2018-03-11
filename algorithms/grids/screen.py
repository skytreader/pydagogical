from components.core import GameScreen, GameLoopEvents
from components.core import Colors

import logging
import pygame

class GridScreen(GameScreen):

    UNTAKEN = Colors.MAX_WHITE
    BLOCKED = Colors.ADVENTURE_DARK

    def __init__(self, config, model):
        super(GridScreen, self).__init__(config, model)

    def draw_screen(self, window):
        self.model.qg.draw(window, self)

class GridLoopEvents(GameLoopEvents):

    def __init__(self, gamescreen):
        super(GridLoopEvents, self).__init__(gamescreen.config, gamescreen)

    def __mouse_click(self):
        self.debug_queue.log("click event detected")
        pos = pygame.mouse.get_pos()
        clicked_cell = self.gamescreen.model.qg.get_clicked_cell(self.gamescreen, pos)
        self.gamescreen.model.toggle(clicked_cell[0], clicked_cell[1])

    def attach_event_handlers(self):
        click_event = pygame.event.Event(pygame.MOUSEBUTTONDOWN)
        self.add_event_handler(click_event, self.__mouse_click)
