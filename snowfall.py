import pygame
pygame.init()#step 1

import random #imported random for random spots on screen 

screen  = pygame.display.set_mode((700,700))#step 2
snow = []

for i in range(50):
    x = random.randrange(0,700)
    y = random.randrange(0,700)
    snow.append([x,y])
#snow contains list of some coordinates randomly made
#so snow list is a 2D list like [[a,b],[c,d],[e,f]]

clock = pygame.time.Clock() #clock object to set framerate how fast the snow falls

while True:                          #step 3
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill('sky blue')
    for ice in range(len(snow)): #in this loop we draw a circle for the coordinate in the snow list
        pygame.draw.circle(screen, 'white', snow[ice],2)
        snow[ice][1]+=1 #we are increasing the y coordinate by one as we want the fall effect 
        if snow[ice][1]>700:  #we put a condition when the coordinate y as we are constantly increasing it 
            #exceeds the lenght of screen we assign a complete new coordinate
            snow[ice][1] = random.randrange(-50,-10)#y is negative as we wanna start from top again and increase y
            snow[ice][0] = random.randrange(0,700)#assigning the x coordinate a new value
    pygame.display.update()
    clock.tick(40)#giving framerate how fast the snow falls by def it is 0 the larger the framerate the slower the snow fall
