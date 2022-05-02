import sys, pygame
from entity import Player, Bullet
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
    diego = Player(controller)
    bulletNum = 0
    bullets = []

    while True:
        map.fill_map(0,0,0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                
                sys.exit()

        if controller.shot() == 1:
            bullets.append(Bullet(diego, 1))
            bulletNum = 1
        if controller.shot() == 2:
            bullets.append(Bullet(diego, 2))
            bulletNum = 1
        if controller.shot() == 3:
            bullets.append(Bullet(diego, 3))
            bulletNum = 1
        if controller.shot() == 4:
            bullets.append(Bullet(diego, 4))
            bulletNum = 1

        if bulletNum > 0:
            print(bulletNum)
            for bullet in bullets:
                bullet.update()
                map.display_object(bullet.image(), bullet.bulletrect())
                print("*********")
            

        
        diego.update()

        # This part should be in the view class
        
        map.display_object(diego.image(), diego.playerrect())
        pygame.display.flip()

        clock.tick(60)

main()
