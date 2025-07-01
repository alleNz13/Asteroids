import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOT_SPEED

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)  
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(velocity)

    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", (int(self.position.x), int(self.position.y)), self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def collide(self, other):
        return self.position.distance_to(other.position) < (self.radius + other.radius)