import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    num = 5
    while(num == 5):
        screen.fill("black")
        pygame.display.flip()
    


if __name__ == "__main__":
    main()
