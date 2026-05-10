from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.rect.x = size_x
        self.rect.y = size_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >5:
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y < 480:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.y < 480:
            self.rect.y += self.speed

        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

window = display.set_mode((700,500))
win_height = 500
display.set_caption('Run')
speed_x = 3
speed_y = 3
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('LOSE PLAYER 1',True, (180,0,0))
lose2 = font1.render('LOSE PLAYER2',True,(180,0,0))
background = transform.scale(image.load('i.webp'), (700,500))
Player1 = Player('хук дк-no-bg-preview (carve.photos).png',300,500,600,100,5)
Player2 = Player('хук дк-no-bg-preview (carve.photos).png',300,500,0,100,5)
Player3 = GameSprite('падж.png',200,200,350,225,2)
finish = False
game = True
clock = time.Clock()
FPS = 60
while game:
    window.blit(background,(0,0))

    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        Player1.update_l()
        Player2.update_r()
        Player3.rect.x += speed_x
        Player3.rect.y += speed_y
        if Player3.rect.y > win_height - 50 or Player3.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(Player1, Player3) or sprite.collide_rect(Player2,Player3):
            speed_x *= -1

        Player1.reset()
        Player2.reset()
        Player3.reset()

    if Player3.rect.x < 0:
        finish = True
        window.blit(lose1, (225, 200))
    if Player3.rect.x > 700:
        finish = True
        window.blit(lose2, (225, 200))

    display.update()
    clock.tick(FPS)
