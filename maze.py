#создай игру "Лабиринт"!
from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def updates(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if key_pressed[K_d] and self.rect.x < 570:
            self.rect.x += self.speed
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 395:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = 'left'
    def updates(self):
        if self.rect.x > 615:
            self.direction = 'left'
        if  self.rect.x < 470:
            self.direction = 'right'
        if self.direction == 'left':
            self.rect.x -= self.speed
        if self.direction == 'right':
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1,color_2,color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x, self.rect.y))



object1 = Enemy('cyborg.png',520,250,1)
object2 = Player('hero.png',5,420,10)
object3 = GameSprite('treasure.png',520,411,1)
window = display.set_mode((700,500))
display.set_caption('dyogonyalochki')
wall1 = Wall(64,228,208,411,134,10,370)
wall2 = Wall(64,228,208,110,134,310,10)
wall3 = Wall(64,228,208,252,70,20,70)
background = transform.scale(image.load('background.jpg'),(700,500))
mixer.init()
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')
font.init()
font = font.SysFont('Arial',40)
win = font.render('You Win',True,(255,215,0))
loose = font.render('You loose',True,(255,215,0))
game = True
finish = False
FPS = 201
clock = time.Clock()
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
        object2.updates()
        object1.updates()
        object1.reset()
        object2.reset()
        object3.reset()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        if sprite.collide_rect(object2,object3):
            finish = True
            money.play()
            window.blit(win,(350,250))
        if sprite.collide_rect(object2,wall1) or sprite.collide_rect(object2,wall2) or sprite.collide_rect(object2,wall3) or sprite.collide_rect(object2,object1):
            finish = True
            kick.play()
            window.blit(loose,(350,250))
    display.update()
    clock.tick(FPS)
