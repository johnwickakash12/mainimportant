import pygame
pygame.init()
window=pygame.display.set_mode((1400,600))
pygame.display.set_caption("Akash koirala")
end=False
while not end:
    for event in pygame.event.get():
        if event.type==pygame.QUIT and event.key == pygame.K_ESCAPE:
            end=True
        if event.type== KEYDOWN and event.key == pygame.K_RIGHT:
            print("you entered right")
        
pygame.exit()