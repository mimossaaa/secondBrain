import pygame
pygame.init()
x = 800
y = 700
scrn = pygame.display.set_mode((x,y))
pygame.display.set_caption('ESW')
imp = pygame.image.load("\\Users\\magne\\Downloads\\258499644_4896749630358090_1493759202484189123_n (1).jpg")
scrn.blit(imp, (0, 0))

pygame.display.flip()
status = True
while (status):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False