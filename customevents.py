import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Custom Events")

COLOR = pygame.USEREVENT +1
BOX_GROW = pygame.USEREVENT +2

bg_color = 'white'
grow = True

box = pygame.Rect((255,255,40,40))

screen.fill('white')

clock = pygame.time.Clock()

pygame.time.set_timer(COLOR, 500)

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            quit()
        if events.type == COLOR:
            if bg_color == 'pink':
                screen.fill('pink')
                bg_color = 'white'
            elif bg_color == 'white':
                screen.fill('white')
                bg_color = 'pink'
        if events.type == BOX_GROW:
            if grow:
                box.inflate_ip(4,4)
                grow = box.width <80
            else:
                box.inflate_ip(-4,-4)
                grow = box.width <40
    if box.collidepoint(pygame.mouse.get_pos()):
        pygame.event.post(pygame.event.Event(BOX_GROW))
    pygame.draw.rect(screen, 'orange',box)
    pygame.display.update()
    clock.tick(40)