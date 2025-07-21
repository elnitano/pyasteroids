import pygame
from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def split(self, screen):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        new_rotation = random.uniform(20, 50)
        rotation_positive = self.velocity.rotate(new_rotation)
        rotation_negative = self.velocity.rotate(new_rotation*-1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_positive = Asteroid(self.position.x, self.position.y, new_radius)
        new_positive.velocity = rotation_positive * 1.2

        new_negative = Asteroid(self.position.x, self.position.y, new_radius)
        new_negative.velocity = rotation_negative * 1.2
