import pygame
pygame.init()
win = pygame.display.set_mode((500,500))
Font = pygame.font.SysFont('timesnewroman',30)
letter = Font.render('Pygame',False,'orange')
i=0#decides speed of text movement
while True:
    if i>500:
        i=0
        pygame.time.wait(500)#wait 5ms

    win.fill('white')
    #moving text at top 
    win.blit(letter,(0,i))#for bottom i,460 left 0,i right 430,i
    i += 80
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.time.wait(500)
    
