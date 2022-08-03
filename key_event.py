import pygame
pygame.init()
screen = pygame.display.set_mode((400,400))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print('A was pressed')
            elif event.key == pygame.K_0:
                print('0 was pressed')
            else:
                print('A key was pressed')