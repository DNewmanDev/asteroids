from circleshape import CircleShape
import pygame
from constants import *
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
        

            

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position[0], self.position[1]), self.radius, 2)
            

    def update(self, dt):
        self.position = self.position + (self.velocity * dt)

    def split(self, screen):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        first_path = self.velocity.rotate(random_angle)
        second_path = self.velocity.rotate(0 - random_angle)
        new_radii = self.radius - ASTEROID_MIN_RADIUS
        new_roid_one=Asteroid(self.position[0], self.position[1], new_radii)
        new_roid_one.velocity = first_path * 1.2
        new_roid_two=Asteroid(self.position[0], self.position[1], new_radii)
        new_roid_two.velocity = second_path *1.2