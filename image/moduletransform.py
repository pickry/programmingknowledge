import pygame
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Loading image')
image = pygame.image.load('japan.jpg')
#image = pygame.transform.flip(image, True, False)
#image = pygame.transform.rotozoom(image, 90,1.5)
#image = pygame.transform.scale2x(image)

print(pygame.transform.average_color(image))
while True:
    screen.fill("white")
    screen.blit(image,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
        
