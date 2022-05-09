"""
Main program to run a game of Diego's Game! Fun fun fun! Weeeeeee.
"""
import sys
import random
import pygame
from entity import Player, Bullet, Enemy
from diegos_game_map import DiegosGameMap
from diegos_game_controller import PlayerController

clock = pygame.time.Clock()
pygame.init()

def main():
    """
    Play a game of Diego's Game.
    """
    # Initialize MVC
    map = DiegosGameMap() # View
    controller = PlayerController() # Controller
    diego = Player(controller, map) # Model

    # Initialize counters
    reload_count = 0
    spawn_count = 0
    difficulty = 0
    score = 0

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

    # Create sprite groups
    diegos = pygame.sprite.Group()
    diegos.add(diego)
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    # Main game loop
    alive = True
    while alive:
        map.fill_map(0,0,0)

        # Check for quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Check delay and shoot
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

        # Check delay and spawn enemy
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

        # Check for bullet/enemy collisions
        for enemy in pygame.sprite.groupcollide(enemies, bullets, 0, 1).keys():
            if enemy.hurt():
                score += 1
            difficulty += 0.02

        # Check for diego/enemy collision
        for diego in pygame.sprite.groupcollide(diegos, enemies, 1, 0).keys():
            alive = False   # End the main loop

        # Draw and update groups of sprites
        map.draw_n_update_groups([bullets, enemies, diegos])

        pygame.display.flip()

        clock.tick(60)  # Cap the framerate

    # End game
    while True:
        map.fill_map(0,0,0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        map.end_screen(score)

        pygame.display.flip()

        clock.tick(60)

main()
