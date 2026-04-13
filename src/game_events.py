"""Game event helpers for handling shared gameplay rules."""

from __future__ import annotations

import pygame


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
