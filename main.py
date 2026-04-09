""" 
Base of the code project
This is the file to run for the project to run
The file has the main loop of the game

"""

import pygame

from player import Player

from config import(
    WIDTH,
    HEIGHT,
    FPS,
    TITLE,
    GRAVITY,
    STARTING_FUEL,
)


## game has to be startet with if __name__ == "__main__" where a single line instaniates the game


def gameloop() -> None:
    """ Run the main game loop.
    
    The loop sets up pygame, loads assets, processes events, updates screen and renders the screen
    """

    pygame.init()

    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption(TITLE)

    clock = pygame.time.Clock()

    player = Player(WIDTH // 2, HEIGHT // 2)

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        player(update)
        screen.fill("black")
        




        pygame.display.flip()

    pygame.quit()



if __name__  == "__main__":
    # run game
    gameloop()
