import pygame
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Moving image')
image = pygame.image.load('San Fransisco.jpeg')
i=0 
while True:
    if i>800:
        i =0
        pygame.time.wait(500)
    screen.fill("white")
    screen.blit(image,(i,0))
    i += 80
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
    pygame.time.wait(500)
