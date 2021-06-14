import pygame
import sys
white=(225,225,225)

def use():
    screen=pygame.display.set_mode((640,480))
    clock=pygame.time.Clock()
    size=pygame.Rect(100, 150, 200, 124)
    while True:
        for event in pygame.event.get():
    
            pygame.display.set_caption("welcome")
            # print(event)
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                sys.exit()
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button== 1:
                    if size.collidepoint(event.pos):
                        print("area click")
            pygame.draw.rect(screen,white,size)
            pygame.display.flip()
            clock.tick(30)


if __name__ == '__main__':
    pygame.init()
    use()
    