"""
Base of the code project
This is the file to run for the project to run
The file has the main loop of the game

Authors: Irjan Evertsen and Emil Olsen-Kristiansen
"""

"""
TODO list
make sure all functions and methods have type hints and doccstrings
clean up duplicate code from merges and unused code
check game feel against requirements, is accelerations implemented correctly?
add needs object and visual health + fuel
"""


import pygame
from src.game_events import get_game_winner, get_game_winner_time, reset_game_winner
from src.player import Player1, Player2
from config import FPS, HEIGHT, TITLE, WIDTH

from src.gui import NeedsDisplay, WinnerAnnouncement, create_center_obstacle, create_fuelcan

##from src.game_events import reverse_ships_if_edge_hit
from src.objects import Ship, Bullet



def gameloop() -> None:
    """ Run the main game loop.

    The loop sets up pygame, loads assets, processes events, updates screen and renders the screen
    """

    pygame.init()
    reset_game_winner()

    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption(TITLE)

    clock = pygame.time.Clock()

    obstacle = create_center_obstacle()

    player1 = Player1(WIDTH // 4, HEIGHT // 4)
    player2 = Player2(WIDTH * 3 // 4, HEIGHT *3 // 4)
    needs_display = NeedsDisplay(player1, player2)

    players = pygame.sprite.Group()
    players.add(player1, player2)

    obstacles = pygame.sprite.Group()
    obstacles.add(obstacle)

    bullets = pygame.sprite.Group()

    fuel_cans = pygame.sprite.Group()


    all_sprites = pygame.sprite.Group()
    all_sprites.add(obstacle, player1, player2, fuel_cans)

    time_from_fuel_spawn = pygame.time.get_ticks()
    fuel_spawn_time = 10000
    winner_show_delay = 3000
    winner_close_delay = 3000

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ## make obstacle


        ## should probably be player1.update(keys) and player2....
        keys = pygame.key.get_pressed()
        winner = get_game_winner()
        winner_time = get_game_winner_time()

        if winner is None:
            players.update(keys, obstacles, players, bullets, fuel_cans)
            bullets.update(players, obstacles)
            winner = get_game_winner()
            winner_time = get_game_winner_time()

        current_time = pygame.time.get_ticks()

        if winner is None and len(fuel_cans) == 0 and current_time - time_from_fuel_spawn > fuel_spawn_time:
            fuel = create_fuelcan()
            fuel_cans.add(fuel)
            all_sprites.add(fuel)
            time_from_fuel_spawn = current_time

        all_sprites.add(bullets)




        screen.fill("black")
        all_sprites.draw(screen)

        needs_display.draw(screen)

        if winner is not None and winner_time is not None:
            time_since_winner = current_time - winner_time

            if time_since_winner >= winner_show_delay:
                winner_announcement = WinnerAnnouncement(winner)
                winner_announcement.draw(screen)

            if time_since_winner >= winner_show_delay + winner_close_delay:
                running = False


        pygame.display.flip()

    pygame.quit()



if __name__ == "__main__":
    # run game
    gameloop()