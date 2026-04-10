"""
Base of the code project
This is the file to run for the project to run
The file has the main loop of the game

Authors: Irjan Evertsen and Emil Olsen-Kristiansen
"""

import pygame
from src.player import Player
from config import FPS, HEIGHT, TITLE, WIDTH
from src.game_events import reverse_ship_if_obstacle_hit, reverse_ships_if_edge_hit
from src.gui import create_center_obstacle, draw_frame
from src.objects import Ship

def gameloop() -> None:
    """ Run the main game loop.

    The loop sets up pygame, loads assets, processes events, updates screen and renders the screen
    """

    pygame.init()

    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption(TITLE)

    clock = pygame.time.Clock()



    ships = pygame.sprite.Group(
        Ship(120, 310, speed_x=3),
        Ship(220, 310, speed_x=3),
        Ship(320, 310, speed_x=3),
    )

    obstacle = create_center_obstacle()

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ships.update()
        reverse_ship_if_obstacle_hit(ships, obstacle)
        reverse_ships_if_edge_hit(ships, WIDTH)

        draw_frame(screen, ships, obstacle)
        pygame.display.flip()

    pygame.quit()



if __name__ == "__main__":
    # run game
    gameloop()

