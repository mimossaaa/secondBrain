
import pygame
pygame.init()
import pygame_menu
from pygame_menu.examples import create_example_window

from typing import Tuple, Any

#surface = create_example_window("MSW", (1000, 870))
screen_width=1000
screen_height=870
screen=pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption('MSW')

def set_difficulty(selected: Tuple, value: Any) -> None:
    
    print(f'Set difficulty to {selected[0]} ({value})')




menu = pygame_menu.Menu(
    height=600,
    theme=pygame_menu.themes.THEME_BLUE,
    
    title='Welcome to the Excelsior Science Workshop',
    width=850
)

#user_name = menu.add.text_input('Name: ', default='Majid R', maxchar=10)
#title = 'Excelsior Science Workshop'

def start_the_game():
    def newscreen(widget, menu):
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
        



    pygame.display.set_caption('image')
    imp = pygame.image.load("\\Users\\magne\\Downloads\\destroylone!!(1).jpg")
    scrn.blit(imp, (0, 0))

    #pygame.display.flip()
    #status = True
    #while (status):
        #for i in pygame.event.get():
            #if i.type == pygame.QUIT:
                #status = False

    
    #global user_name
    #print(f'{user_name.get_value()}, Do the job here!')


menu.add.selector('What do you like? ', [('Building', 1), ('Animals', 2), ('Rocks', 3), ('Bones', 4)], onchange=set_difficulty)
#button = menu.add_button('This button updates its padding', None)
#button.set_draw_callback(newscreen)

menu.add.button('Enter', start_the_game)

    
#menu.add.button('Quit', pygame_menu.events.EXIT)

if __name__ == '__main__':
    menu.mainloop(screen)
    