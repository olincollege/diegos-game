import sys, pygame
from entity import Player, Bullet
from diegos_game_map import DiegosGameMap
from diegos_game_controller import PlayerController

clock = pygame.time.Clock()
pygame.init()

size = width, height = 600, 400
black = 0, 0, 0

screen = pygame.display.set_mode(size)

diegoimage = pygame.image.load("diego.png")
#diegorect = diego.get_rect()
#diegospeed = [2, 0]

def main():
    map = DiegosGameMap()
    controller = PlayerController(map)
    diego = Player(controller)
    bullet = Bullet(diego)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                
                sys.exit()
        
        diego.update()
        bullet.update()

        # This part should be in the view class
        screen.fill((0, 0, 0))
        screen.blit(diego.image(), diego.playerrect())
        screen.blit(bullet.image(), bullet.bulletrect())
        pygame.display.flip()

        clock.tick(60)

main()
