"""
Diego's game controller.
"""
import pygame

class PlayerController():
    """
    Keyboard based controller for the game that takes keystrokes from WASD and
    arrow keys.

    Attributes:
        moving_right: A boolean flag indicating a pressed D key.
        moving_left: A boolean flag indicating a pressed A key.
        moving_up: A boolean flag indicating a pressed W key.
        moving_down: A boolean flag indicating a pressed S key.
    """
    moving_right = False
    moving_left = False
    moving_up = False
    moving_down = False

    def __init__(self):
        """
        No initialization needs to be done for the controller
        """

    def get_movement(self):
        """
        Get keystrokes from the WASD keys on the keyboard to control the
        player.

        Returns:
            A list of boolean key flags representing which keys are pressed.
        """
        keystate = pygame.key.get_pressed()

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        if keystate[pygame.K_a]:
            self.moving_left = True
        if keystate[pygame.K_d]:
            self.moving_right = True
        if keystate[pygame.K_w]:
            self.moving_up = True
        if keystate[pygame.K_s]:
            self.moving_down = True

        return [
            self.moving_left,
            self.moving_right,
            self.moving_up,
            self.moving_down
            ]

    def shot(self):
        """
        Get keystrokes from the arrow keys on the keyboard to control the
        player's shots.

        Returns:
            A number representing which key is pressed.
            2:right, 4:left, 1:up, 3:down, 5:other
        """
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_RIGHT]:
            return 2
        if keystate[pygame.K_LEFT]:
            return 4
        if keystate[pygame.K_UP]:
            return 1
        if keystate[pygame.K_DOWN]:
            return 3
        return 5
