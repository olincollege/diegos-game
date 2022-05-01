from abc import abstractclassmethod, abstractmethod
import sys, pygame
from abc import ABC, abstractmethod

class Entity(ABC, pygame.sprite.Sprite):

    def __init__(self):
        pass

    @abstractmethod
    def update(self):
        pass


class Character(Entity):
    _position = [0, 0]
    _velocity = [0, 0]
    _health = 5

    @abstractmethod
    def update(self):
        pass


class Player(Character):
    def __init__(self):
        self._image = pygame.image.load("diego.png")
        self._playerrect = self._image.get_rect()

    def playerrect(self):
        return self._playerrect

    def image(self):
        return self._image

    def update(self):
        self._position[0] += self._velocity[0]
        self._position[1] += self._velocity[1]
        self._playerrect = self._playerrect.move(self._velocity)