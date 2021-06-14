import pygame
import sys
screenheight=800
screenwidth=800
white=(225,225,225)
red=(225,0,0)
pygame.init()
window=pygame.display.set_mode((screenheight,screenwidth))
size=pygame.Rect(200, 200, 220, 220)
while True:
    for event in pygame.event.get():
    
        pygame.display.set_caption("welcome")
        # print(event)
        if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
            sys.exit()
        if event.type==pygame.QUIT:
            sys.exit()
    pygame.draw.rect(window, white, size)
    pygame.display.update()