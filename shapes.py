import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('draw')

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            quit()
        
    screen.fill('pink')
    pygame.draw.polygon(screen,'green',((140,0),(140,80),(180,120),(220,80),(220,0)))
    pygame.draw.ellipse(screen, 'blue',(200,250,100,50))
    pygame.draw.arc(screen,'yellow',(300,300,80,40),1.5708,3.14159,8)
    pygame.draw.lines(screen,'black',False,((0,200),(100,100),(200,200),(300,100),(400,200)),5)
    pygame.display.update()