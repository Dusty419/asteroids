# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    asteroidField = AsteroidField()
    

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for item in updatable:
            item.update(dt)
        for asteroid in asteroids:
            if asteroid.collision_detection(player):
                print("Game over!")
                sys.exit()
            
            for shot in shots:
                if asteroid.collision_detection(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill("black")
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()