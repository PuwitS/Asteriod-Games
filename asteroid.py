import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        #could play around more with for loop to create i astroids
        astroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        astroid1.velocity = self.velocity.rotate(random_angle) * 1.2
        astroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        astroid2.velocity = self.velocity.rotate(-random_angle) * 1.2
        
