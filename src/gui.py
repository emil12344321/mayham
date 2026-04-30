"""GUI helpers for creating and drawing game visuals.

Authors: Irjan Evertsen and Emil Olsen-Kristiansen
"""

from __future__ import annotations

import pygame
import random

from config import HEIGHT, OBSTACLE_COLOR, OBSTACLE_SIZE, WIDTH, FUEL_COLOR, FUEL_SIZE
from src.objects import Obstacle, Fuel


def create_center_obstacle() -> Obstacle:
	"""Create a static obstacle centered in the game window."""
	return Obstacle(
		x=(WIDTH - OBSTACLE_SIZE[0]) // 2,
		y=(HEIGHT - OBSTACLE_SIZE[1]) // 2,
		size=OBSTACLE_SIZE,
		color=OBSTACLE_COLOR,
	)

def create_fuelcan() -> Fuel:
	"""Create fuel can in random position"""
	obstacle_rect = pygame.Rect(
		(WIDTH - OBSTACLE_SIZE[0]) // 2,
		(HEIGHT - OBSTACLE_SIZE[1]) // 2,
		OBSTACLE_SIZE[0],
		OBSTACLE_SIZE[1],
	)

	while True:
		fuel = Fuel(
			x=random.randint(0, WIDTH - FUEL_SIZE[0]),
			y=random.randint(0, HEIGHT - FUEL_SIZE[1]),
			size=FUEL_SIZE,
			color=FUEL_COLOR,
		)

		if not fuel.rect.colliderect(obstacle_rect):
			return fuel


def draw_frame(screen: pygame.Surface, ships: pygame.sprite.Group, obstacle: Obstacle) -> None:
	"""Draw one frame of the game scene."""
	screen.fill("black")
	obstacle.draw(screen)
	ships.draw(screen)