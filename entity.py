from abc import abstractclassmethod, abstractmethod
import sys, pygame
from abc import ABC, abstractmethod

SPEED = 1

class Entity(ABC, pygame.sprite.Sprite):
    _position = [0, 0]
    _velocity = [0, 0]

    def __init__(self):
        pass

    @property
    def position(self):
        return self._position

    @property
    def velocity(self):
        return self._velocity

    @abstractmethod
    def update(self):
        pass


class Character(Entity):
    _health = 5

    @abstractmethod
    def update(self):
        pass


class Player(Character):
    def __init__(self, controller, map):
        self._image = pygame.image.load("diego.png")
        self._playerrect = self._image.get_rect()
        self._controller = controller
        self._map = map

    @property
    def playerrect(self):
        return self._playerrect

    @property
    def velocity(self):
        return (self._velocity[0], self._velocity[1])

    def image(self):
        return self._image

    def update(self):
        self._velocity[0] = 0
        self._velocity[1] = 0

        keys = self._controller.get_movement()
        if keys[0]: # Left
            self._velocity[0] = -1 * SPEED
        if keys[1]: # Right
            self._velocity[0] = 1 * SPEED
        if keys[2]: # Up
            self._velocity[1] = -1 * SPEED
        if keys[3]: # Down
            self._velocity[1] = 1 * SPEED
        
        self._position[0] += self._velocity[0]
        self._position[1] += self._velocity[1]
        self._playerrect = self._playerrect.move(self._velocity)
        self._playerrect = self._playerrect.clamp(self._map.screenrect)


class Bullet(Entity, pygame.sprite.Sprite):
    def __init__(self, player, map, direction):
        pygame.sprite.Sprite.__init__(self)
        self._position = player.position
        self._map = map
        self.image = pygame.image.load("bullet.png")
        self.rect = self.image.get_rect(center=(player.playerrect.centerx, player.playerrect.centery))
        #self._bulletrect = self._image.get_rect(center=player.position)
        #self._bulletrect = self._bulletrect.move(player._playerrect().centerx, player._playerrect().centery)
        if direction == 1:
            self._velocity = player.velocity[0],player.velocity[1]-2
        if direction == 2:
            self._velocity = player.velocity[0]+2,player.velocity[1]
        if direction == 3:
            self._velocity = player.velocity[0],player.velocity[1]+2
        if direction == 4:
            self._velocity = player.velocity[0]-2,player.velocity[1]

    def bulletrect(self):
        return self.rect

    def image(self):
        return self.image

    def position(self):
        return self._position

    # def touching_border(self, size):
    #     if 0 > self._bulletrect.left or self._bulletrect.left > size[0]:
    #         self.kill()
    #     if 0 > self._bulletrect.top or self._bulletrect.top > size[0]:
    #         self.kill()

    def update(self):
        print(self._velocity)

        self._position[0] += 0#self._velocity[0]
        self._position[1] += 0#self._velocity[1]
        self.rect = self.rect.move(self._velocity)

        if(
            self.rect.top < self._map.screenrect.top
            or self.rect.bottom > self._map.screenrect.bottom
            or self.rect.left < self._map.screenrect.left
            or self.rect.right > self._map.screenrect.right
        ):
            self.kill()