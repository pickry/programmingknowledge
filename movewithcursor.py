import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))
#load the image want to move around
img = pygame.image.load('left/spaceship.png')

#get the rectangle surface for the image 
rect = img.get_rect(center = (250//2,250//2))
moving = False#the boolean for cursor's state if it is in motion or not
while True:
    screen.fill('white')
    screen.blit(img, rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP:
            moving = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            rect.collidepoint(event.pos)#test if the event's position is inside a rectangle
            moving = True
        elif event.type == pygame.MOUSEMOTION and moving:
            rect.move_ip(event.rel)#same as rect.move but moves the rectangle in place
    
    
    
    pygame.display.update()