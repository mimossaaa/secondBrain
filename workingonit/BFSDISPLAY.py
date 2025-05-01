import pygame
import sys 

pygame.init()
x = 800
y = 700
scrn = pygame.display.set_mode((x,y))
pygame.display.set_caption('BFS')
imp = pygame.image.load("\\Users\\magne\\Downloads\\BFSLOGO.png")
scrn.blit(imp, (0, 0))
color = (255,255,255)
color_light = (170,170,170)  
color_dark = (100,100,100) 
#smallfont = pygame.font.SysFont('Helvetica',35) 
#text = smallfont.render('quit' , True , color) 
#while True: 
      
    #for ev in pygame.event.get(): 
          
        #if ev.type == pygame.QUIT: 
            #pygame.quit() 
              
        #checks if a mouse is clicked 
        #if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            #if the mouse is clicked on the 
            # button the game is terminated 
            #if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
                #pygame.quit() 
                  
    # fills the screen with a color 
    #scrn.fill((60,25,60)) 
      
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    #mouse = pygame.mouse.get_pos() 
  
pygame.display.flip()
status = True
while (status):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False