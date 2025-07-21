# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from circleshape import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    pyclock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shoot = pygame.sprite.Group()
    Player.containers = (updatable, drawable, shoot)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shoot, drawable, updatable)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        dt = pyclock.tick(60) / 1000

        updatable.update(dt)

        for astoroid in asteroids:
            if astoroid.check_collision(player):
                raise sys.exit("Game over!")
            for shots in shoot:
                if astoroid.check_collision(shots):
                    astoroid.split(screen)
                    shots.kill()

        for objects in drawable:
            objects.draw(screen)

        pygame.display.flip()
        

if __name__ == "__main__":
    main()
