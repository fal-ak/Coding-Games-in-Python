#Game 3 Of PYTHON
#Flappy Bird
#Made by pygame

import pygame

import sys

import random

pygame.init()

 
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Flappy Bird")

FPS = 30

WHITE = (255, 255, 255)

BLACK = (0, 0, 0)

BIRD_SIZE = 100

OBSTACLE_WIDTH = 300

OBSTACLE_HEIGHT = random.randint(100, 270 )

OBSTACLE_GAP = 150

PURPLE = (128, 0, 128 )

background_image = pygame.image.load("C:\\Users\\USER\\Desktop\\Coding Games in Python\\bg.jpeg").convert_alpha() 


background_image = pygame.transform.scale(background_image, (800, 600))


bird_image = pygame.image.load("C:\\Users\\USER\\Desktop\\Coding Games in Python\\flappy bird.png").convert_alpha()

bird_image = pygame.transform.scale(bird_image, (BIRD_SIZE, BIRD_SIZE))


obstacle_image = pygame.image.load("C:\\Users\\USER\\Desktop\\Coding Games in Python\\obstacles.png").convert_alpha()

obstacle_image = pygame.transform.scale(obstacle_image, (OBSTACLE_WIDTH, 600))

font = pygame.font.Font( None, 72) 



class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = bird_image
        self.rect = self.image.get_rect(center=(100, 600 // 2))

        self.velocity = 0
        self.alive = True

    def update(self):
        if self.alive:
            self.velocity += 1
            self.rect.y += self.velocity
            if self.rect.bottom >= 600:
                self.alive = False



class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = obstacle_image
        self.rect = self.image.get_rect(topleft=(800, 0))

    def update(self):
        self.rect.x -= 5

        if self.rect.right < 0:
            self.rect.x = 800
            self.rect.height = random.randint(50, 900)


all_sprites = pygame.sprite.Group()

obstacles = pygame.sprite.Group()


bird = Bird()
all_sprites.add(bird)


clock = pygame.time.Clock()

run = True

obstacle_frequency = 0 



while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.velocity = -15



    screen.blit(background_image, (0, 0))



    all_sprites.update()
    
    obstacles.update()



    if bird.alive:
        collisions = pygame.sprite.spritecollide(bird, obstacles, False)


    if collisions:
        bird.alive = False

    if bird.alive and obstacles:
        collisions = pygame.sprite.spritecollide(bird, obstacles, False)


    if collisions:
        bird.alive = False


    obstacle_frequency += 2


    if obstacle_frequency % 100 == 0:  
        obstacle = Obstacle()

        obstacles.add(obstacle)

        all_sprites.add(obstacle)


    if bird.alive:

        all_sprites.draw(screen)
        

    if not bird.alive:

        game_over_text = font.render("Game Over", True, (128, 0, 128  ))

        screen.blit(game_over_text, (800 // 2 - game_over_text.get_width() // 2, 600 // 2 - game_over_text.get_height() // 2))

    

    pygame.display.flip()

    clock.tick(FPS)


pygame.quit()
sys.exit()