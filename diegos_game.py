import sys, pygame

pygame.init()

size = width, height = 320, 240
black = 0, 0, 0

screen = pygame.display.set_mode(size)

diego = pygame.image.load("diego.png")
diegorect = diego.get_rect()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                
                sys.exit()
        screen.fill(black)
        screen.blit(diego, diegorect)
        pygame.display.flip()
main()