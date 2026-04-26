from pygame import *
window = display.set_mode((700,500))
display.set_caption('Run')
background = transform.scale(image.load('i.webp'), (700,500))
game = True
while game:
    window.blit(background,(0,0))

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
