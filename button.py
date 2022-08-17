import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('pygame button')

font = pygame.font.SysFont('Georgia',40,bold=True)
surf = font.render('Quit', True, 'white')
button = pygame.Rect(200,200,110,60)

while True:
    screen.fill('pink')
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
        if events.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(events.pos):
                pygame.quit()
    a,b = pygame.mouse.get_pos()
    if button.x <= a <= button.x + 110 and button.y <= b <= button.y +60:
        pygame.draw.rect(screen,(180,180,180),button )
    else:
        pygame.draw.rect(screen, (110,110,110),button)
    screen.blit(surf,(button.x +5, button.y+5))
    pygame.display.update()