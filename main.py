import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Shot

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
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)


    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroids_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #object update      
        for object in updatable:
            object.update(dt)
        #collision check
        for asteroid in asteroids:
            if player.collision(asteroid):
                pass
                #print("Game Over!")
                #sys.exit()
                
            for bullet in shots:
                if asteroid.collision(bullet):
                    bullet.kill()
                    asteroid.split()

        screen.fill("black")
        #draw objet
        for object in drawable:        
            object.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000
            

if __name__ == "__main__":
    main()

'''
Could add:
-Scoring system
-live and respawning
-effects(mainly astroid explode)
-acceleration to player movement
-object wrap around the screen instead of disappearing
-more weapons!
-differnet asteroid shape
-fix player hitbox
-power ups!
-main menu, gameover screen
'''