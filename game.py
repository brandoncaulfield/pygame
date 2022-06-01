import pygame
from pygame.locals import *
import time


# define a main function
def main():
     
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    GRAY = (150, 150, 150)
    

    # initialize the pygame module
    pygame.init()

    
    
    # Title
    pygame.display.set_caption("Text Game")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((1200,800))

    text = 'this text is editable'
    font = pygame.font.SysFont(None, 24)
    img = font.render(text, True, BLUE)

    rect = img.get_rect()
    rect.topleft = (20, 20)
    cursor = Rect(rect.topright, (3, rect.height))
    
    
    

    # define a variable to control the main loop
    running = True

     # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    if len(text)>0:
                        text = text[:-1]
                else:
                    text += event.unicode
                img = font.render(text, True, RED)
                rect.size=img.get_size()
                cursor.topleft = rect.topright
        
        screen.fill((255, 255, 0))
        screen.blit(img, rect)
        
        if time.time() % 1 > 0.5:
            pygame.draw.rect(screen, RED, cursor)
    
        pygame.display.update()

        



# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()