import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Jump!")

my_rect = pygame.Rect(200,200,10,20)
speed = 5

jump = False
jumpC = 10


while True:
    pygame.time.delay(100)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and my_rect.x>0:
        my_rect.x -= speed
    if keys[pygame.K_RIGHT] and my_rect.x<500 - my_rect.w:
        my_rect.x += speed
    if keys[pygame.K_UP] and my_rect.y >0:
        my_rect.y -= speed
    if keys[pygame.K_DOWN] and my_rect.y<500 - my_rect.h:
        my_rect.y += speed

    if jump == False:
        if keys[pygame.K_SPACE]:
            jump = True
    else:
        if jumpC >= -10:
            my_rect.y -= (jumpC * abs(jumpC)) * 0.5
            jumpC -= 1
        else:
            jump = False
            jumpC = 10

    screen.fill((130,222,134))
    pygame.draw.rect(screen,'purple',my_rect)
    pygame.display.update()