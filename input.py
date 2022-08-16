import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('user input')

user_ip = ''
font = pygame.font.SysFont('frenchscript',40)
text_box = pygame.Rect(75,75,100,50)
active = False
color = pygame.Color('purple')
clock = pygame.time.Clock()

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            quit()
        if events.type == pygame.MOUSEBUTTONDOWN:
            if text_box.collidepoint(events.pos):
                active = True
            else:
                active = False
        if events.type == pygame.KEYDOWN:
            if active:
                if events.key == pygame.K_BACKSPACE:
                    user_ip = user_ip[:-1]
                else:
                    user_ip += events.unicode
    screen.fill('pink')
    if active:
        color = pygame.Color('red')
    else:
        color = pygame.Color('purple')
    pygame.draw.rect(screen,color, text_box,4)
    surf = font.render(user_ip,True,'orange')
    screen.blit(surf, (text_box.x +5 , text_box.y +5))
    text_box.w = max(100, surf.get_width()+10)
    pygame.display.update()
    clock.tick(50)