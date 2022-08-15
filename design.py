import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Designs')

x,y = 100,100
width, height = 10,10
speed = 10

while True:
    pygame.time.delay(10)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    key = pygame.key.get_pressed()

    if key[pygame.K_UP] and y>0:
        y -= speed
    if key[pygame.K_DOWN] and y<500-height:
        y += speed
    if key[pygame.K_LEFT] and x>0:
        x -= speed
    if key[pygame.K_RIGHT] and x<500 -width:
        x += speed
    
    pygame.draw.rect(screen, 'white', (x,y, width, height))
    pygame.display.update()
    
