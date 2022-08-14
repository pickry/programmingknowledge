import pygame 
pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Types of cursors")

#there are 3 types of cursors colored, system, and bitmap
system = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND)#system

bitmap = pygame.cursors.Cursor(pygame.cursors.broken_x)#bitmap


sur = pygame.Surface((10, 10)) 
sur.fill('sky blue')        
color = pygame.cursors.Cursor((5, 5), sur)#colored

pygame.mouse.set_cursor(system)#setting system cursor as initial cursor

clock = pygame.time.Clock()

while True:
    clock.tick(60)
    screen.fill('pink')
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()    
        if event.type == pygame.MOUSEBUTTONDOWN: #if mouse is clicked use the bitmap cursor
            pygame.mouse.set_cursor(bitmap)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:#if c key is pressed use the color cursor
                pygame.mouse.set_cursor(color)
    pygame.display.flip()

