"""
Diego's game map/view implementation.
"""
import pygame
from pygame.locals import *


class DiegosGameMap():
    """
    Pygame window view of diego's game map.
    """

    def __init__(self):
        """
        Create a new, empty map.
        """
        self._size = width, height = 320, 240
        self._screenrect = Rect(0, 0, width, height)
        self._background = (0, 0, 0)
        self.screen = pygame.display.set_mode(self._size)

    @property
    def screenrect(self):
        """
        Return the screen's rect.
        """
        return self._screenrect

    def size(self):
        """
        Return the screen's size.
        """
        return self._size

    def background(self):
        """
        Return the background color.
        """
        return self._background

    def fill_map(self, red, green, blue):
        """
        Fill the window's background with a solid color

        Args:
            red: integer representing the red value of the color.
            green: integer representing the green value of the color.
            blue: integer representing the blue value of the color.
        """
        self.screen.fill((red, green, blue))

    def end_screen(self, score):
        """
        Put up the end splash screen when you die.

        Args:
            score: integer representing the final score of the game.
        """
        font = pygame.font.Font(None, 72)
        text1 = font.render('Game Over', True, (255, 0, 0))
        text_rect1 = text1.get_rect()
        text_rect1.centerx = self._screenrect.centerx
        text_rect1.centery = self._screenrect.centery - 25

        text2 = font.render(str(score), True, (255, 255, 255))
        text_rect2 = text2.get_rect()
        text_rect2.centerx = self._screenrect.centerx
        text_rect2.centery = self._screenrect.centery + 25

        self.screen.blit(text1, text_rect1)
        self.screen.blit(text2, text_rect2)

    def draw_n_update_groups(self, groups):
        """
        Draw and update all groups of sprites on screen.

        Args:
            groups: list of pygame sprite groups.
        """
        for group in groups:
            group.draw(self.screen)
            group.update()
