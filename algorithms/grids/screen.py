from components.common_ui import Button
from components.core import GameScreen, GameLoopEvents
from components.core import Colors

import logging
import pygame

class GridScreen(GameScreen):

    UNTAKEN = Colors.MAX_WHITE
    BLOCKED = Colors.ADVENTURE_DARK

    def __init__(self, config, model):
        super(GridScreen, self).__init__(config, model)

    def setup(self):
        self.simulate_button = Button("Find Path", Colors.HUMAN_BLUE, (428, 128))
        self.simulate_button.set_event_handler(
            pygame.event.Event(pygame.MOUSEBUTTONDOWN), self.simulate_handler
        )
        self.ui_elements.add(self.simulate_button)

    def simulate_handler(self, event):
        pos = pygame.mouse.get_pos()
        if self._is_drawable_clicked(self.simulate_button, pos):
            print "Hello world."

    def draw_screen(self, window):
        self.model.qg.draw(window, self)

    def draw_unchanging(self, window):
        self.simulate_button.draw(window, self)

class GridLoopEvents(GameLoopEvents):

    def __init__(self, gamescreen):
        super(GridLoopEvents, self).__init__(gamescreen)

    def __mouse_click(self, ev):
        pos = pygame.mouse.get_pos()
        clicked_cell = self.game_screen.model.qg.get_clicked_cell(self.game_screen, pos)
        if clicked_cell:
            self.game_screen.model.toggle(clicked_cell[0], clicked_cell[1])

    def attach_event_handlers(self):
        super(GridLoopEvents, self).attach_event_handlers()
        click_event = pygame.event.Event(pygame.MOUSEBUTTONDOWN)
        self.add_event_handler(click_event, self.__mouse_click)
