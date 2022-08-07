import pygame
pygame.init()#step 1

screen = pygame.display.set_mode((500,500)) #step 2
pygame.display.set_caption('Moving the given object') #setting up a caption
x = 100
y = 100 # initial coordinate of the object to be moved
speed = 3  # set up the speed at which the object moves on one press
width = 10
height = 7  # setting up the size of the object taken a rectangle object
while True:
    pygame.time.delay(10)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill('yellow')
    key  = pygame.key.get_pressed()
    
    #Returns a sequence of boolean values representing the state of every key on the keyboard. 
    #Use the key constant values to index the array. Example, key[pygame.K_LEFT]
    # A True value means that the button is pressed.
    #the conditions for which the object moves on screen
    if key[pygame.K_LEFT] and x>0:#left key then left move with the given vel
        x -= speed
        print('left arrow key')
    if key[pygame.K_RIGHT] and x<500-width:
        x += speed
        print('right arrow key')
    if key[pygame.K_UP] and y>0:
        y -= speed
        print('up arrow key')
    if key[pygame.K_DOWN] and y<500-height:
        y += speed
        print('down arrow key')
    pygame.draw.rect(screen, 'dark green',(x,y,width, height))#make my figure
    pygame.draw.circle(screen, 'darkgreen', (x+5,y-5),5)
    pygame.display.update()

    