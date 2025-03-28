from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white", self.position, self.radius,2)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            angle = random.uniform(20,50)
            v1 = self.velocity.rotate(angle)
            v2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position, self.position, new_radius)
            a2 = Asteroid(self.position, self.position, new_radius)
            a1.velocity = v1 * 1.2
            a2.velocity = v2 * 1.2
            self.kill()

            
