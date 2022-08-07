import pygame
pygame.init()#to initialize pygame  
#pygame.display.init()
'''to uninitializ we use quit'''


''' 
The display.set_mode() function creates a new Surface object which helps us visualize whatever we create image, text, drawing etc.'''
#display : Pygame has a single display Surface that is either contained in a window or runs full screen
'''some methods of display module are   set_mode, get_init,quit, init,get_surface : reference to current window
flip update fill 
update update portions of screen optimized version of flip'''
screen = pygame.display.set_mode((600,600))

#Rect(left, top, width, height) -> Rect 
'''Rect objects to store and manipulate rectangular areas. '''
ball = pygame.image.load('ball.jpg')
ballrect = ball.get_rect()#ball rect is a rect class objct
#copy move inflate update clip clamp fit collide 
#copy
#move(x,y)/ move in place move_ip() "line 74 for example "
#inflate change size only integers (-2,2)
#update sets new position new in pygame 2.0.1
#clamp moves the rectangle in another
#clip crops rect inside another also clipline
#fit resize with aspect ratio
#collide point if a point is inside rect
#colide rect test if two rects overlap



'''event : Pygame handles all its event messaging through an event queue. The routines
 in this module help you manage that event queue.
 The event queue has an upper limit on the number of events it can hold (128 for standard SDL 1.2). When the queue becomes full 
 new events are quietly dropped. To prevent loss of events, especially input events which signal a quit command, your program must handle events 
 every frame (with pygame.event.get(), pygame.event.pump(), pygame.event.wait(),
 pygame.event.peek() or pygame.event.clear()) and process them
'''


'''Whenever a key is pressed or released, pygame.event() queue methods pygame.KEYDOWN and pygame.KEYUP events respectively.
pygame.key.get_focused : true if the display is receiving keyboard input from the system
pygame.key.get_pressed: get the state of all keyboard buttons
pygame.key.name : get the name of a key identifier
pygame.key.key_code : get the key identifier from a key name
pygame.key.start_text_input : start handling Unicode text input events
pygame.key.stop_text_input : stop handling Unicode text input events
pygame.key.set_text_input_rect : controls the position of the candidate list'''

#key for involving keyboard if input is taken from key board .get_focused

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_a:
#                 print('A was pressed')
#             elif event.key == pygame.K_0:
#                 print('0 was pressed')
#             else:
#                 print('A key was pressed')


speed = [2,0]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    ballrect = ballrect.move(speed) #becuase ball rect was an object of Rect
    if ballrect.left < 0 or ballrect.right > 800:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > 800:
        speed[1] = -speed[1]

    screen.fill((255,255,255))
    screen.blit(ball, ballrect)
    pygame.display.flip()
'''font'''
#font : can test if font moudule is initialized, get the default font, know all
#the fonts available, can create a new font object from a file etc
# pygame.font.Font bold, italic, underline, render,size
'''image: loading unloading changing format saving image,
 time: delay pause has clock method to keep track of time control framerate , 
 music : rewind stop play etc, 
 draw for shapes circles polygons'''



#surface : A pygame Surface is used to represent any image uses bitmap. The Surface has a fixed resolution and pixel format. 
'''pygame.Surface.blit : draw one image onto another
pygame.Surface.blits : draw many images onto another
pygame.Surface.convert :change the pixel format of an image
pygame.Surface.copy :create a new copy of a Surface
pygame.Surface.fill: fill Surface with a solid color
pygame.Surface.scroll :Shift the surface image in place
pygame.Surface.get_at: get the color value at a single pixel
pygame.Surface.set_at : set the color value for a single pixel
'''



