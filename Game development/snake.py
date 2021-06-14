import pygame
import pygame
import random
pygame.init()
#colors
white=(225,225,225)
red=(225,0,0)
black=(0,0,0)
#window initializing
screen_width=1200
screen_height=600
# snake_x=600
# snake_y=300
window=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("snake game by Akash")
pygame.display.update()

# Variables
# foodx=random.randint(20,screen_width/2)
# foody=random.randint(20, screen_height/2)
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)
# snake_velx=0
# snake_vely=0
# game_end=False
# fps=30
# init_velocity=5
# snk_list=[]
# snakelenght=1
# size=15
# score=0
# images['background']=pygame.image.load('images/download.jpg')
def text_screen(text,color,x,y):
    screentext=font.render(text, True, color)
    window.blit(screentext,[x,y])

def snakeplot(window,color,snk_list,size):
    for x,y in snk_list:
        pygame.draw.rect(window, color, [x,y,size,size])



def Gameloop():
    foodx=random.randint(20,screen_width/2)
    foody=random.randint(20, screen_height/2)
    snake_x=600
    snake_y=300
    
    snake_velx=0
    snake_vely=0
    game_end=False
    game_over=False
    fps=30
    init_velocity=10
    snk_list=[]
    snakelenght=1
    size=15
    score=0
    while not game_end:
        if game_over:
            window.fill(white)
            text_screen("Game over press Enter to continue and escape to stop", red, 100, 250)
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN and event.key==pygame.K_RETURN:
                    Gameloop()
                if event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    game_end=True
                if event.type== pygame.QUIT:
                    game_end=True
        else:
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        Gameloop()
                if event.type== pygame.QUIT or(event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    game_end=True
                if event.type==pygame.KEYDOWN and event.key==pygame.K_UP:
                    snake_vely-=init_velocity
                    snake_velx=0
                if event.type==pygame.KEYDOWN and event.key==pygame.K_DOWN:
                    snake_vely+=init_velocity
                    snake_velx=0
                if event.type==pygame.KEYDOWN and event.key==pygame.K_LEFT:
                    snake_velx-=init_velocity
                    snake_vely=0
                if event.type==pygame.KEYDOWN and event.key==pygame.K_RIGHT:
                    snake_velx+=init_velocity
                    snake_vely=0

            snake_x+=snake_velx
            snake_y+=snake_vely

            if abs(snake_x-foodx)<10 and abs(snake_y-foody)<10:
                score+=10
                foodx=random.randint(20,screen_width/2)
                foody=random.randint(20, screen_height/2)
                snakelenght+=5
            window.fill(white)
            text_screen("Your Score is "+str(score), red, 5, 5)
            pygame.draw.rect(window, black, [foodx,foody,size,size])


            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snakelenght:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over=True
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True
            snakeplot(window, red, snk_list, size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
Gameloop()