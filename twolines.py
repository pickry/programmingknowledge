import pygame
pygame.init()

screen = pygame.display.set_mode((800,500))
pygame.display.set_caption("Text!")

text = "Hello everyone! \nWe are trying to display text on pygame window."
font = pygame.font.SysFont("Inkfree",60)

def display_text(surface, text, pos, font, color):
    collection = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    x,y = pos
    for lines in collection:
        for words in lines:
            word_surface = font.render(words, True, color)
            word_width , word_height = word_surface.get_size()
            if x + word_width >= 800:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x,y))
            x += word_width + space
        x = pos[0]
        y += word_height


while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill('pink')
    display_text(screen, text, (20,20), font, 'purple')
    pygame.display.update()