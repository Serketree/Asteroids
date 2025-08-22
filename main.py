import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # type: ignore
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    aster = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    Asteroid.containers = (aster, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (bullets, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # type: ignore
    asteroid_spawner = AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill("black")

        for asteroid in aster:
            if asteroid.check_collision(player):
                print("Game over!")
                return
        for asteroid in aster:
            for shot in bullets:
                if shot.check_collision(asteroid):
                    shot.kill()
                    asteroid.split()

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
