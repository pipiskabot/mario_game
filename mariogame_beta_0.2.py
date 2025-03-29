import pygame
import sys
pygame.init()

W_width = 1200
W_height = 600
FPS = 20
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
ADD_NEW_FLAME_RATE = 25

cactus_img = pygame.image.load('cactus_bricks.png')
cactus_img_rect = cactus_img.get_rect()
cactus_img_rect.left = 0
fire_img = pygame.image.load('fire_bricks.png')
fire_img_rect = fire_img.get_rect()
fire_img_rect.left = 0

CLOCK = pygame.time.pygame.time.Clock()

font = pygame.font.SysFont('forte', 20)

canvas = pygame.display.set_mode((W_width, W_height))
pygame.display.set_caption('Mario')

class Topscore:
    def __init__(self):
        self.hight_score = 0

    def top_score(self, score):
        if score > self.hight_score:
            self.hight_score = score
        return self.hight_score

topscore = Topscore()

class Dragon:
    dragon_velocity = 10

    def __init__(self):
        self.dragon_img = pygame.image.load('dragon.png')
        self.dragon_img_rect = self.dragon_img.get_rect()
        self.dragon_img_rect.width -= 10
        self.dragon_img_rect.height -= 10
        self.dragon_img_rect.top = W_height/2
        self.dragon_img_rect.right = W_width
        self.up = True
        self.down = False

    def update(self):
        canvas.blit(self,dragon_img, self.dragon_img_rect)
        if self.dragon_img_rect.top <= cactus_img_rect.bottom:
            self.up = False
            self.down = True

        elif self.dragon_img_rect.bottom >= fire_img_rect.top:
            self.up = True
            self.down = False
        
        if self.up:
            self.dragon_img_rect.top -= self.dragon_velocity
        elif self.down:
            self.dragon_img_rect.top += self.dragon_velocity

class Flames:
    flames_velocity = 20

    def __init__(self):
        self.flames = pygame.image.load('fireball.png')
        self.flames_img = pygame.transform.scale(self.flames, (20, 20))
        self.flames_img_rect = self.flames_img.get_rect()
        self.flames_img_rect.right -= dragon.dragon_img_rect.left
        self.flames_img_rect.top = dragon.dragon_img_rect.top + 30
    
    def update(self):
        canvas.blit(self.flames_img, self.flames_img_rect)
        
        if self.flames_img_rect.left > 0:
            self.flames_img_rect -= self.flames_velocity

class Mario:
    velocity = 10

    def __init__(self):
        self.mario_img = pygame.image.load('maryo.png')
        self.mario_img_rect = self.mario_img.get_rect()
        self.mario_img_rect.left = 20
        self.mario_img_rect.top = W_height/2 - 100
        self.down = True
        self.up = False

    def update(self):
        canvas.blit(self.mario_img, self.mario_img_rect)
        
        if self.mario_img_rect.top <= cactus_img_rect.bottom or self.mario_img_rect.top >= fire_img_rect.bottom:
            game_over()
            if SCORE < self.mario_score:
                self.mario_score = SCORE




        if self.up:
            self.mario_img_rect.top -= 10

        if self.down:
            self.mario_img_rect.bottom += 10

def game_over():
    pygame.mixer.music.stop()
    music = pygame.mixer.Sound('mario_dies.wav')
    music.play()
    topscore.top_score(SCORE)
    game_over_img = pygame.image.load('end.png')
    game_over_img_rect = game_over_img.pygame.get_rect()
    game_over_img_rect.center = (W_height/2, W_width/2)
    canvas.blit(game_over_img, game_over_img_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.tipe == pygame.KEYDOWN:
                event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        pygame.display.update()