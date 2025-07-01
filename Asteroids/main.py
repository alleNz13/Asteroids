import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from bullet import Shot


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
   
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time_clock = pygame.time.Clock()
    dt = 0
    tick_rate = 60
    drawables = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()
    
    Player.containers = (updatables,drawables)  
    Asteroid.containers = (asteroid_group, drawables, updatables)
    AsteroidField.containers = (updatables,)
    Shot.containers = (bullet_group, drawables, updatables)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) 
    asteroid_field = AsteroidField()
    
    
        
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatables.update(dt)
        screen.fill((0,0,0), None, 0)
        for drawable in drawables:
            drawable.draw(screen)
        for asteroid in asteroid_group:
            if asteroid.collide(player):
                print("Game Over!")
                exit(0)
            for bullet in bullet_group:
                if bullet.collide(asteroid):
                    asteroid.split()
                    bullet.kill()
                    break
        pygame.display.flip()
        time_clock.tick(tick_rate)
        dt = time_clock.tick(tick_rate) / 1000.0  







if __name__ == "__main__":
    main()