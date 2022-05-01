import sys, pygame

pygame.init()

size = width, height = 320, 240
black = 0, 0, 0

screen = pygame.display.set_mode(size)

diego = pygame.image.load("diego.png")
diegorect = diego.get_rect()
diegospeed = [2, 0]

def main():
    global diegorect
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                
                sys.exit()

        diegorect = diegorect.move(diegospeed)

        if diegorect.left < 0 or diegorect.right > width:
            diegospeed[0] = -diegospeed[0]

        screen.fill(black)
        screen.blit(diego, diegorect)
        pygame.display.flip()

main()