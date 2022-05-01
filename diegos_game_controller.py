"""
Diego's game controller.
"""
import sys, pygame
from abc import ABC, abstractmethod

class PlayerController(ABC):
    """
    """
    moving_right = False
    moving_left = False
    moving_up = False
    moving_down = False

    def __init__(self, map):
        """
        """
        self._map = map

    @property
    def map(self):
        """
        """
        return self._map

    def get_movement(self):
        """
        """
        keystate = pygame.key.get_pressed()

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        if keystate[pygame.K_LEFT]:
            self.moving_left = True
        if keystate[pygame.K_RIGHT]:
            self.moving_right = True
        if keystate[pygame.K_UP]:
            self.moving_up = True
        if keystate[pygame.K_DOWN]:
            self.moving_down = True

        return [
            self.moving_left,
            self.moving_right,
            self.moving_up,
            self.moving_down
            ]
        