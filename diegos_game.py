import sys, pygame
from entity import Player, Bullet, Enemy
from diegos_game_map import DiegosGameMap
from diegos_game_controller import PlayerController

clock = pygame.time.Clock()
pygame.init()

#size = width, height = 600, 400
#black = 0, 0, 0

#screen = pygame.display.set_mode(size)



def main():
    map = DiegosGameMap()
    controller = PlayerController(map)
    diego = Player(controller, map)
    reloadCount = 0

    enemies = pygame.sprite.Group()
    enemies.add(Enemy(diego, map))

    bullets = pygame.sprite.Group()

    while True:
        map.fill_map(0,0,0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                
                sys.exit()
        if reloadCount < 0:
            if controller.shot() == 1:
                bullets.add(Bullet(diego, map, 1))
                reloadCount = 30
            if controller.shot() == 2:
                bullets.add(Bullet(diego, map, 2))
                reloadCount = 30
            if controller.shot() == 3:
                bullets.add(Bullet(diego, map, 3))
                reloadCount = 30
            if controller.shot() == 4:
                bullets.add(Bullet(diego, map, 4))
                reloadCount = 30
        reloadCount -= 1

        bullets.update()
        bullets.draw(map.screen)
        enemies.update()
        enemies.draw(map.screen)
        #print(diego.velocity)
        
        diego.update()

        # This part should be in the view class
        
        map.display_object(diego.image(), diego.playerrect)
        pygame.display.flip()

        clock.tick(60)

main()
