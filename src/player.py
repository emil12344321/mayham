"""
This file has the player script of the game

"""



## should have :
"""
player pos (self.x and self.y)
velocity
angle (self.angle)
ship image (self.image)
hitbox (self.x, self.y)
update()
draw()
"""



import math
import pygame

from config import GRAVITY, STARTING_FUEL, THRUST, WIDTH, HEIGHT, STARTING_HEALTH, FUEL_COOLDOWN
from src.objects import Ship, Obstacle, Bullet

"""
Todo
make code more object oriented. could probably use the same
class and some form of polymorhpism

"""


"""
Base player class, owns movement, physics, collison, rotation and drawing of player object
Player1, Player2 own controls (input) and colour
"""

class Player(Ship):
    def __init__(self, x, y, color, controls):
        super().__init__(x,y, size=(40,40))

        self.controls = controls
        self.color = color

        #player constants
        self.rotation_speed = 3
        self.thrust = THRUST
        self.radius = 18
        self.gravity = GRAVITY

        # Needs holder fuel og health for enhver spiller
        self.needs = Needs()
        self.is_alive = True

        ## fuel cooldown makes the fuel drain less time per frame
        self.fuel_cooldown = FUEL_COOLDOWN
        self.last_fuel = 0

        self.bullet_cooldown = 300 # miliseconds
        self.last_shot = 0

        # update player image
        self.original_image = self.create_ship_surface()
        self.image = self.original_image
        self.update_rect()


    def create_ship_surface(self) -> pygame.Surface:
        surface = pygame.Surface((40,40), pygame.SRCALPHA)
        pygame.draw.polygon(surface, self.color, [(20,0), (5,35),(35,35)])
        pygame.draw.rect(surface, "white", (17, 10, 6, 6))
        return surface

    def collision(self, obstacle) -> bool:
        pointx = max(obstacle.rect.left, min(self.x, obstacle.rect.right))
        pointy = max(obstacle.rect.top, min(self.y, obstacle.rect.bottom))

        dx = self.x - pointx
        dy = self.y - pointy

        return (dx * dx + dy * dy) < (self.radius * self.radius)


    # changed to use circle hitbox
    def inside_screen(self) -> None:
        if self.x - self.radius < 0:
            self.x = self.radius
            self.vx = -self.vx / 4

        if self.x + self.radius > WIDTH:
            self.x = WIDTH - self.radius
            self.vx = -self.vx / 4

        if self.y - self.radius < 0:
            self.y = self.radius
            self.vy = -self.vy / 4

        if self.y + self.radius > HEIGHT:
            self.y = HEIGHT - self.radius
            self.vy = -self.vy / 4

        self.update_rect()

    def shoot(self, bullets) -> None:
        time = pygame.time.get_ticks()

        if time - self.last_shot < self.bullet_cooldown:
            return


        bullet = Bullet(self.x, self.y, self.angle, self)
        bullets.add(bullet)

        self.last_shot = time

    ### Fuel methods, TODO Change these when the needs object is added, this logic is temporery
    def pick_up_fuel(self, fuel_cans) -> None:
        fuel_touch = pygame.sprite.spritecollide(self, fuel_cans, True, pygame.sprite.collide_circle)

        ## change this with needs object
        if fuel_touch:
            self.needs.add_fuel(STARTING_FUEL // 2)


    def update(self, keys, obstacles, players, bullets, fuel_cans) -> None:
        #rotation
        old_x = self.x
        old_y = self.y

        # gravity
        self.vy += self.gravity

        # check for fuel
        self.pick_up_fuel(fuel_cans)

        #movement
        self.move()

        self.inside_screen()

        #input
        self.handle_input(keys, bullets)

        # rotate playerimage
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.update_rect()

        for obstacle in obstacles:
            if self.collision(obstacle):
                self.undo_movement(old_x, old_y)

        sprite_collision = pygame.sprite.spritecollide(self, players, False, pygame.sprite.collide_circle)


        for player in sprite_collision:
            if player != self:
                self.undo_movement(old_x, old_y)
                break


    def undo_movement(self, old_x, old_y) -> None:
        self.x = old_x
        self.y = old_y
        self.vx = -self.vx
        self.vy = -self.vy + 1
        self.update_rect()

    def handle_input(self, keys, bullets) -> None:
        if keys[self.controls["left"]]:
            self.angle += self.rotation_speed

        if keys[self.controls["right"]]:
            self.angle -= self.rotation_speed

        if keys[self.controls["up"]] and self.needs.has_fuel():
            radians = math.radians(self.angle)
            self.vx -= (math.sin(radians) * self.thrust)/3
            self.vy -= math.cos(radians) * self.thrust
            
            curr_time = pygame.time.get_ticks()

            if curr_time - self.last_fuel >= self.fuel_cooldown:
                self.needs.use_fuel(1)
                self.last_fuel = curr_time
        
        if keys[self.controls["shoot"]]:
            self.shoot(bullets)


    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)


class Player1(Player):
    def __init__(self, x: float, y: float) -> None:
        controls = {
            "left": pygame.K_LEFT,
            "right": pygame.K_RIGHT,
            "up": pygame.K_UP,
            "shoot": pygame.K_RSHIFT,
        }

        super().__init__(x, y, "blue", controls)



class Player2(Player):
    def __init__(self, x: float, y: float) -> None:
        controls = {
            "left": pygame.K_a,
            "right": pygame.K_d,
            "up": pygame.K_w,
            "shoot": pygame.K_SPACE,
        }

        super().__init__(x, y, "red", controls)


class Needs:
    "Holder status for enhver spiller"
    def __init__(self) -> None:
        self.max_fuel = STARTING_FUEL
        self.fuel = STARTING_FUEL
        self.health = STARTING_HEALTH

    def has_fuel(self) -> bool:
        """Returns true if the player still has fuel"""
        if self.fuel > 0:
            return True
    
    def use_fuel(self, amount: int) -> None:
        """Method for player using fuel, used by thrust"""
        self.fuel = max(0, (self.fuel - amount))

    def add_fuel(self, amount: int) -> None:
        """Adds fuel to the player by the given amount"""
        self.fuel = min(self.max_fuel, self.fuel + amount)
