""" 
Base of the code project
This is the file to run for the project to run
The file has the main loop of the game

"""

import pygame

from config import(
    WIDTH,
    HEIGHT,
    FPS,
    TITLE,
    BACKGROUND_IMAGE,
    GRAVITY,
    STARTING_FUEL,
)


## game has to be startet with if __name__ == "__main__" where a single line instaniates the game


def gameloop() -> None:
    """ Run the main game loop.
    
    The loop sets up pygame, loads assets, processes events, updates screen and renders the screen
    """

    pygame.init()



if __name__  == "__main__":
    # run game
    gameloop()
