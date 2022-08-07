import pygame
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Loading image')
image = pygame.image.load('San Fransisco.jpeg')
imagerect = image.get_rect()
imagerect.center = ((800//2,400//2))
while True:
    screen.fill("white")
    screen.blit(image,imagerect) #using the rect object
    #screen.blit(image,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
        
