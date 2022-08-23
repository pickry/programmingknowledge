import pygame
pygame.init()
import time

import random

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Collision Game!')

clock = pygame.time.Clock()
speed = 5
font = pygame.font.SysFont('Georgia',60)

class Brick(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('collision/brick.png')
        self.image = pygame.transform.scale(self.image,(40,40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,500-40),0)
    
    def move(self):
        self.rect.move_ip(0,speed)
        if self.rect.top>500:
            self.rect.top = 0
            self.rect.center = (random.randint(30,470),0)

class Man(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('collision/scared man.jpg')
        self.image = pygame.transform.scale(self.image,(100,150))
        self.rect = self.image.get_rect()
        self.rect.center = (200,420)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-5,0)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(5,0)

M1 = Man()
B1 = Brick()

bricks = pygame.sprite.Group()
bricks.add(B1)

all_sprites = pygame.sprite.Group()
all_sprites.add(M1)
all_sprites.add(B1)



while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill('white')

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(M1, bricks):
        text = font.render('Game Over',True, 'orange')
        textrect = text.get_rect(center = (500//2,500//2))
        screen.blit(text,textrect)
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()

    pygame.display.flip()
    clock.tick(60)