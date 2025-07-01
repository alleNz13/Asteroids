import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOT_SPEED, PLAYER_SHOOT_COOLDOWN
from circleshape import CircleShape
from bullet import Shot 


class Player(CircleShape):
    
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.rotation = 0  # Player's rotation angle in degrees
        self.timer = 0
        


    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt


    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        
        if self.timer <= 0:
            new_shot_velocity = pygame.Vector2(0, 1).rotate(self.rotation)
            bullet_velocity = new_shot_velocity * PLAYER_SHOT_SPEED
            new_shot = Shot(self.position.x, self.position.y, bullet_velocity)
            self.timer += PLAYER_SHOOT_COOLDOWN

        
            