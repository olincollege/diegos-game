"""
Diego's game controller.
"""
import sys, pygame
from abc import ABC, abstractmethod

class player_controller(ABC):
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

    def movement(self):
        """
        """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moving_right = True
                if event.key == pygame.K_LEFT:
                    moving_left = True
                if event.key == pygame.K_UP:
                    moving_up = True
                if event.key == pygame.K_DOWN:
                    moving_down = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    moving_right = False
                if event.key == pygame.K_LEFT:
                    moving_left = False
                if event.key == pygame.K_UP:
                    moving_up = False
                if event.key == pygame.K_DOWN:
                    moving_down = False
        return [moving_down, moving_left, moving_right, moving_up]