import sys, pygame
import random

from scipy.fftpack import diff
from entity import Player, Bullet, Enemy
from diegos_game_map import DiegosGameMap
from diegos_game_controller import PlayerController

clock = pygame.time.Clock()
pygame.init()

#size = width, height = 600, 400
#black = 0, 0, 0

#screen = pygame.display.set_mode(size)



def main():
    # Initialize MVC
    map = DiegosGameMap()
    controller = PlayerController(map)
    diego = Player(controller, map)

    # Initialize counters
    reload_count = 0
    spawn_count = 0
    difficulty = 0

    # Load sprite images
    enemy_images = (
        pygame.image.load("enemy1.png"),
        pygame.image.load("enemy2.png"),
        pygame.image.load("enemy3.png")
    )
    Enemy.images = enemy_images

    bullet_images = (
        pygame.image.load("bullet.png"),
        None
    )
    Bullet.images = bullet_images

    diegos = pygame.sprite.Group()
    diegos.add(diego)

    enemies = pygame.sprite.Group()

    bullets = pygame.sprite.Group()

    while True:
        map.fill_map(0,0,0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                
                sys.exit()
        if reload_count < 0:
            if controller.shot() == 1:
                bullets.add(Bullet(diego, map, 1))
                reload_count = 30
            if controller.shot() == 2:
                bullets.add(Bullet(diego, map, 2))
                reload_count = 30
            if controller.shot() == 3:
                bullets.add(Bullet(diego, map, 3))
                reload_count = 30
            if controller.shot() == 4:
                bullets.add(Bullet(diego, map, 4))
                reload_count = 30
        reload_count -= 1
        
        if spawn_count < 0:
            rand = random.random()
            if rand > 0.3:
                enemies.add(Enemy(diego, map, health=1, speed=0.5))
            elif rand > 0.1:
                enemies.add(Enemy(diego, map, health=2, speed=0.3))
            else:
                enemies.add(Enemy(diego, map, health=3, speed=0.2))
            spawn_count = 60*1.7
        spawn_count -= 1 + difficulty

        for enemy in pygame.sprite.groupcollide(enemies, bullets, 0, 1).keys():
            enemy.hurt()
            difficulty += 0.03
            print('Difficulty: ', difficulty)

        for diego in pygame.sprite.groupcollide(diegos, enemies, 1, 0).keys():
            print('You died!')
            pygame.quit()
            sys.exit()

        bullets.update()
        bullets.draw(map.screen)
        enemies.update()
        enemies.draw(map.screen)
        diegos.update()
        diegos.draw(map.screen)

        # This part should be in the view class
        
        
        pygame.display.flip()

        clock.tick(60)

main()
