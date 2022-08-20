import pygame
pygame.init()
import math

screen = pygame.display.set_mode((1000,500))

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            quit()
    t = pygame.time.get_ticks()/3 % 1000
    x = t
    y = math.sin(t/50)*100 +200
    pygame.draw.circle(screen, 'white',(x,y),10)
    pygame.display.update()