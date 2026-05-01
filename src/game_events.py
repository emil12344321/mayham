"""Game event helpers for handling shared gameplay rules.

Authors: Irjan Evertsen and Emil Olsen-Kristiansen
"""

from __future__ import annotations

import pygame

game_winner_player = None
game_winner_time = None
player_scores = {
    "Player1": 0,
    "Player2": 0,
}


def reverse_ship_if_obstacle_hit(ships: pygame.sprite.Group, obstacle: pygame.sprite.Sprite) -> bool:
	"""Reverse only ships that collide with the obstacle.

	Returns True if at least one ship changed direction this frame.
	"""
	hit_any_ship = False

	for ship in ships:
		if not hasattr(ship, "rect"):
			continue
		if not hasattr(ship, "reverse_direction"):
			continue
		if not hasattr(obstacle, "rect"):
			continue

		if ship.rect.colliderect(obstacle.rect):
			hit_any_ship = True

			# Push ship outside the obstacle before reversing to avoid oscillation.
			if hasattr(ship, "speed_x") and ship.speed_x >= 0:
				ship.rect.right = obstacle.rect.left
			else:
				ship.rect.left = obstacle.rect.right

			ship.reverse_direction()

	return hit_any_ship


def reverse_ships_if_edge_hit(ships: pygame.sprite.Group, screen_width: int) -> bool:
	"""Reverse all ships when any ship touches a horizontal edge.

	Returns True if a direction change was applied this frame.
	"""
	should_reverse = any(
		hasattr(ship, "hits_screen_edge") and ship.hits_screen_edge(screen_width)
		for ship in ships
	)

	if should_reverse:
		for ship in ships:
			if hasattr(ship, "reverse_direction"):
				ship.reverse_direction()

	return should_reverse


def bullet_hit_player(bullet, player) -> None:
    from config import BULLET_DAMAGE

    player.needs.health = max(0, player.needs.health - BULLET_DAMAGE)
    bullet.kill()

    if player.needs.health == 0 and player.is_alive:
        player_died(player, bullet.owner)


def player_died(player, killer) -> None:
    """Mark a player as dead and pass the killer to the winner handler."""
    player.is_alive = False
    player.kill()
    game_winner(killer)


def game_winner(winner) -> None:
    """Store the winner, update score and when the game ended."""
    global game_winner_player, game_winner_time

    if game_winner_player is not None:
        return

    game_winner_player = winner
    game_winner_time = pygame.time.get_ticks()

    winner_name = winner.__class__.__name__
    if winner_name in player_scores:
        player_scores[winner_name] += 1


def get_game_winner():
    """Return the winner if the game has ended."""
    return game_winner_player


def get_game_winner_time():
    """Return when the winner was decided."""
    return game_winner_time


def get_scores():
    """Return a copy of the current player scores."""
    return player_scores.copy()


def reset_game_winner() -> None:
    """Clear winner state before a new game starts."""
    global game_winner_player, game_winner_time

    game_winner_player = None
    game_winner_time = None
