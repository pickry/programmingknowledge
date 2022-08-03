import pygame
#for creating video games basically easy to use as beginners
#to work with audio, texts, images etc.
#games like snake game, tic tac toe, binary search implementation, space game, moving objects, drawing shapes
#learn about a lot of methods and functions in pygame
#three parts only basic 
from pygame.locals import *
pygame.init()#to call all functionalities

#for understanding colors rgb
#red = (0,200,255)
#orange = (200,0,200)
#setting the screen
screen = pygame.display.set_mode((200,200))#initialize screen
#font = pygame.font.Font('freesansbold.ttf',24)#the font desc
#text = font.render('hello kitty..',True,red)#the text desc


#textrect = text.get_rect()#the text rect don't know yet


#textrect.center = (200//2 , 200 //2)#for display in centre'''
# a game loop
while True:
    screen.fill((200,0,0))#background
    #screen.blit(text, textrect)#call on display 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
     
            # deactivates the pygame library
            pygame.quit()
 
            # quit the program.
            quit()
 
        # Draws the surface object to the screen.
        pygame.display.update()#print everytime till no data available

#differnce between update and flip
#events in pygame
#clock
#framerate

