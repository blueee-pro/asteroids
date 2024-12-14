import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField


updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatable, drawable)
AsteroidField.containers = (updatable)
Asteroid.containers = (asteroids, updatable, drawable)
Shot.containers = (shots, updatable, drawable)

def main():
    pygame.init()


    clock = pygame.time.Clock()
    dt = 0
    score = 0
    time_lived = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        screen.fill("black")

        time_lived += dt

        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        font = pygame.font.Font(None, 36)
        time_lived_text = font.render(f'Time Lived: {time_lived:.1f}', True, (255, 255, 255))
        screen.blit(time_lived_text, (10, 50))

        for entity in drawable:
            entity.draw(screen)
        for entity in updatable:
            entity.update(dt)

        
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                import sys
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if shot.check_collision(asteroid):
                    score += asteroid.split()
                    shot.kill()

       
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()