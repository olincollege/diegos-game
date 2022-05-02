"""
Diego's game map implementation.
"""
import sys, pygame


class DiegosGameMap():
    """
    
    """

    def __init__(self):
        """
        Create a new, empty map.
        """
        # Writing the following ensures that each square of the board is
        # independent from each other. Writing something like
        # [[" "] * 3] * 3
        # will cause the board to be made up of copies of the same cell,
        # resulting in strange behavior.
        self._size = width, height = 320, 240
        self._background = (0, 0, 0)
        self.screen = pygame.display.set_mode(self._size)

    def size(self):
        """
        """
        return self._size

    def background(self):
        """
        """
        return self._background

    def fill_map(self, r, g, b):
        """
        """
        self.screen.fill((r, g, b))

    def display_object(self, image, rect):
        """
        """
        self.screen.blit(image, rect)

    def display_bullet(self, image, rect, x, y):
        """
        """
        self.screen.blit(image, rect, (x, y))


    #def check_win(self):
        #