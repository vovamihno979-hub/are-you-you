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
display.set_caption('Run')
background = transform.scale(image.load('i.webp'), (700,500))
Player1 = Player('хук дк-no-bg-preview (carve.photos).png',300,500,600,100,1)
Player2 = Player('хук дк-no-bg-preview (carve.photos).png',300,500,0,100,1)
Player3 = GameSprite('падж.png',200,200,350,225,2)
finish = False
game = True
while game:
    window.blit(background,(0,0))

    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        Player1.update_l()
        Player1.reset()
        Player2.update_r()
        Player2.reset()
        Player3.reset()


    display.update()
