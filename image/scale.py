#Image Scaling refers to the resizing of the original image
import pygame
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Scaling')
image = pygame.image.load('San Fransisco.jpeg')
image = pygame.transform.scale(image,(400,400))

while True:
    screen.fill('white')
    screen.blit(image, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()

