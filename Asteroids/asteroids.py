import pygame
from circleshape import CircleShape
import random
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def  __init__(self,x,y,radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.new_angle = random.randint(20, 50)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid1.velocity = self.velocity.rotate(self.new_angle) * 1.2
            new_asteroid2.velocity = self.velocity.rotate(-self.new_angle) *1.2
            
            
        