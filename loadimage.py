import pygame
pygame.init()
screen = pygame.display.set_mode((800,800))
image = pygame.image.load('San Fransisco.jpeg')
while True:
    for event in pygame.events.get():
        