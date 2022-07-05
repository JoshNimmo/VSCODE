#print("hello world")

import pygame
pygame.init()
x = 1
screen = pygame.display.set_mode((400,400))
color = pygame.Color(255,0,0)
black = pygame.Surface((400,400))
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        move()
    pygame.quit()

def move():
    global x
    global black
    x += 1
    screen.blit(black,(0,0))
    pygame.draw.rect(screen,color,pygame.Rect(x,0,100,100))
    pygame.display.flip()

main()