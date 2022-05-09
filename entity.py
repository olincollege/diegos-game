from abc import abstractclassmethod, abstractmethod
import sys, pygame
from abc import ABC, abstractmethod
import random
import math

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

class Enemy(Character):
    _health = 3
    _speed = 0.5
    images = ()
    def __init__(self, player, map, health=1, speed=0.5):
        pygame.sprite.Sprite.__init__(self)
        self._health = health
        self._speed = speed
        self.image = self.images[self._health - 1]
        self._map = map
        self._player = player

        # start_position = (
        #     random.randrange(0, self._map.screenrect.right),
        #     random.randrange(0, self._map.screenrect.bottom)
        # )
        distance = math.hypot(self._map.screenrect.width, self._map.screenrect.height) + 5
        start_position = (
            distance*math.cos(random.random()*2*math.pi),
            distance*math.sin(random.random()*2*math.pi)
        )

        self.rect = self.image.get_rect(center=(start_position))
        self._position = start_position

    def hurt(self):
        self._health = self._health - 1
        self.image = self.images[self._health - 1]
        if self._health <= 0: self.kill()

    def update(self):
        distance_to_player = math.hypot(
            self.rect.centerx - self._player.playerrect.centerx,
            self.rect.centery - self._player.playerrect.centery
        )
        x_comp = 0
        y_comp = 0
        if distance_to_player != 0:
            x_comp = (self._player.playerrect.centerx - self.rect.centerx)/distance_to_player
            y_comp = (self._player.playerrect.centery - self.rect.centery)/distance_to_player
        self._position = (self._position[0] + x_comp*self._speed, self._position[1] + y_comp*self._speed)
        self.rect.center = self._position


class Player(Character):
    def __init__(self, controller, map):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("diego.png")
        self.rect = self.image.get_rect(center=(map.screenrect.center))
        self._controller = controller
        self._map = map

    @property
    def playerrect(self):
        return self.rect

    @property
    def velocity(self):
        return (self._velocity[0], self._velocity[1])

    def image(self):
        return self.image

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
        self.rect = self.rect.move(self._velocity)
        self.rect = self.rect.clamp(self._map.screenrect)


class Bullet(Entity, pygame.sprite.Sprite):
    images = ()

    def __init__(self, player, map, direction):
        pygame.sprite.Sprite.__init__(self)
        self._position = player.position
        self._map = map
        self.image = self.images[0]
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
        self._position[0] += 0#self._velocity[0]
        self._position[1] += 0#self._velocity[1]
        self.rect.move_ip(self._velocity)

        if(
            self.rect.top < self._map.screenrect.top
            or self.rect.bottom > self._map.screenrect.bottom
            or self.rect.left < self._map.screenrect.left
            or self.rect.right > self._map.screenrect.right
        ):
            self.kill()