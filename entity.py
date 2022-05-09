"""
Entity classes implementation.
"""

from abc import ABC, abstractmethod
import random
import math
import pygame

SPEED = 0.2

class Entity(ABC, pygame.sprite.Sprite):
    """
    Abstract base class for all entities/sprites.

    Attributes:
        _position: position on screen of entity
        _velocity: velocity of entity
    """
    _position = [0, 0]
    _velocity = [0, 0]

    def __init__(self):
        pass

    @property
    def position(self):
        """
        Return entity's position.
        """
        return self._position

    @property
    def velocity(self):
        """
        Return entity's velocity.
        """
        return self._velocity

    @abstractmethod
    def update(self):
        """
        Abstract method for updating entity.
        """


class Enemy(Entity):
    """
    Enemy class implementation with basic player following algorithm.

    Attributes:
        images: tuple of images for the sprite.
    """
    images = ()

    def __init__(self, player, map, health=1, speed=0.5):
        """
        Spawn a new enemy at a random position on the screen.

        Args:
            player: an instance of the Player class.
            map: an instance of the DiegosGameMap class.
            health: an integer representing the health of the enemy. Default=1.
            speed: an float representing the speed of the enemy. Default=0.5.
        """
        pygame.sprite.Sprite.__init__(self)
        self._health = health
        self._speed = speed
        self.image = self.images[self._health - 1]
        self._map = map
        self._player = player

        distance = math.hypot(
            self._map.screenrect.width, self._map.screenrect.height
            ) + 5
        start_position = (
            distance*math.cos(random.random()*2*math.pi),
            distance*math.sin(random.random()*2*math.pi)
        )

        self.rect = self.image.get_rect(center=(start_position))
        self._position = start_position

    def hurt(self):
        """
        Hurt the enemy, decreasing health by one. The enemy's color will either
        change, or the enemy will die if it is on one health.

        Returns:
            True if the enemy dies, False if the enemy is still alive after
            getting hurt.
        """
        self._health = self._health - 1
        self.image = self.images[self._health - 1]
        if self._health <= 0:
            self.kill()
            return True
        return False

    def update(self):
        """
        Update position of enemy. The enemy will track the player and move
        towards the player's position in a straight line.
        """
        distance_to_player = math.hypot(
            self.rect.centerx - self._player.playerrect.centerx,
            self.rect.centery - self._player.playerrect.centery
        )
        x_comp = 0
        y_comp = 0
        if distance_to_player != 0:
            x_comp = (
                (self._player.playerrect.centerx - self.rect.centerx)
                /distance_to_player
            )
            y_comp = (
                (self._player.playerrect.centery - self.rect.centery)
                /distance_to_player
            )
        self._position = (
            self._position[0] + x_comp*self._speed,
            self._position[1] + y_comp*self._speed
        )
        self.rect.center = self._position


class Player(Entity):
    """
    Player class implementation with basic keyboard movement.
    """
    def __init__(self, controller, map):
        """
        Spawn a new player in the center of the screen.

        Args:
            controller: an instance of the PlayerController class.
            map: an instance of the DiegosGameMap class.
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("diego.png")
        self.rect = self.image.get_rect(center=(map.screenrect.center))
        self._position = self.rect.center
        self._controller = controller
        self._map = map

    @property
    def playerrect(self):
        """
        Return the player's rect.
        """
        return self.rect

    @property
    def velocity(self):
        """
        Return the player's velocity.
        """
        return self._velocity

    def image(self):
        """
        Return the player's sprite image.
        """
        return self.image

    def update(self):
        """
        Update position of player based on velocity and keyboard input. The
        player has inertia, which helps with aiming and hitting angle shots.
        """
        self._velocity[0] *= 0.9
        self._velocity[1] *= 0.9

        keys = self._controller.get_movement()
        if keys[0]: # Left
            self._velocity[0] -= 1 * SPEED
        if keys[1]: # Right
            self._velocity[0] += 1 * SPEED
        if keys[2]: # Up
            self._velocity[1] -= 1 * SPEED
        if keys[3]: # Down
            self._velocity[1] += 1 * SPEED

        self._position = (
            self._position[0] + self._velocity[0],
            self._position[1] + self._velocity[1]
        )
        self.rect.center = self._position


class Bullet(Entity, pygame.sprite.Sprite):
    """
    Bullet class implementation.

    Attributes:
        images: tuple of images for the sprite.
    """
    images = ()

    def __init__(self, player, map, direction):
        """
        Spawn a new bullet in the center of the player.

        Args:
            player: an instance of the Player class.
            map: an instance of the DiegosGameMap class.
            direction: an integer representing the direction of the bullet.
            1:up, 2:right, 3:down, 4:left
        """
        pygame.sprite.Sprite.__init__(self)
        self._map = map
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=player.playerrect.center)
        self._position = self.rect.center
        if direction == 1:
            self._velocity = player.velocity[0],player.velocity[1]-2
        if direction == 2:
            self._velocity = player.velocity[0]+2,player.velocity[1]
        if direction == 3:
            self._velocity = player.velocity[0],player.velocity[1]+2
        if direction == 4:
            self._velocity = player.velocity[0]-2,player.velocity[1]

    def bulletrect(self):
        """
        Return the bullet's rect.
        """
        return self.rect

    def image(self):
        """
        Return the bullet's sprite image.
        """
        return self.image

    def position(self):
        """
        Return the bullet's position
        """
        return self._position

    def update(self):
        """
        Update position of bullet. If the bullet goes off the screen, kill it.
        """
        self._position = (
            self._position[0] + self._velocity[0],
            self._position[1] + self._velocity[1]
        )
        self.rect.center = self._position

        if(
            self.rect.top < self._map.screenrect.top
            or self.rect.bottom > self._map.screenrect.bottom
            or self.rect.left < self._map.screenrect.left
            or self.rect.right > self._map.screenrect.right
        ):
            self.kill()
