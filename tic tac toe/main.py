import pygame
import sys
screenheight=800
screenwidth=800
white=(225,225,22)
special=(28,170,156)
special2=(23,135,145)
pygame.init()
window=pygame.display.set_mode((screenheight,screenwidth))
size=20
# size1=pygame.Rect(250,70,20,700)
# # location variables
# # first row
# sqx=20
# sqy=70
# size2=pygame.Rect(480, 70, 20, 700)

# size4=pygame.Rect(20,250,700,20)

# size7=pygame.Rect(20, 500, 700, 20)
# # sqx_5=20
# size8=pygame.Rect(250,530,220,220)
# size9=pygame.Rect(480,530,220,220)
# sqy_3=490
# sqx_6=230
# sqx_7=440
cross=pygame.image.load('gallery/cross.png')
window.fill(special)
pygame.draw.line(window,special2,(250,0),(250,900),20)
pygame.draw.line(window,special2,(540,0),(540,900),20)
pygame.draw.line(window,special2,(0,260),(900,260),20)
pygame.draw.line(window,special2,(0,500),(900,500),20)
while True:
    
    # window.fill(red)
    
    for event in pygame.event.get():

        pygame.display.set_caption("welcome")
        # print(event)
        if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
            sys.exit()
        if event.type==pygame.QUIT:
            sys.exit()
        
    if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button == 1:#left button
                if box1.collidepoint(event.pos):
                    
                    window.blit(cross, (0,0))
    # box1=pygame.draw.rect(window,white,size1)
    # box2=pygame.draw.rect(window,white,size2)

    
    # box4=pygame.draw.rect(window,white,size4)
    
    # box7=pygame.draw.rect(window,white,size7)

    pygame.display.update()