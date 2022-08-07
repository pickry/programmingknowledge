#Image Rotation refers to the turning of an image with some angle. Rotations in the coordinate plane are counterclockwise
import pygame
pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Rotating')
image = pygame.image.load('japan.jpg')
image = pygame.transform.rotate(image, -90)

while True:
    screen.fill("white")
    screen.blit(image,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
    