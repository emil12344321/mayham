"""Game event helpers for handling shared gameplay rules.

Authors: Irjan Evertsen and Emil Olsen-Kristiansen
"""

from __future__ import annotations

import pygame


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
