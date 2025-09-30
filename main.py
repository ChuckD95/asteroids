import pygame, sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #frame limiter
    clock = pygame.time.Clock()
    dt = 0
    #groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Asteroid.containers = (updatables, drawables, asteroids)
    AsteroidField.containers = (updatables)
    Shot.containers = (updatables, drawables)
    #print(updatables)
    #print(drawables)

    #player object
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    asteroidfield = AsteroidField()
    #asteroid = Asteroid(0,0,5)
    #print(updatables)
    #print(drawables)
    
    while 1 > 0:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(pygame.Color('black'))
        #player.update(dt)
        #player.draw(screen)
        updatables.update(dt)
        for drawable in drawables:
            drawable.draw(screen)

        for asteroid in asteroids:
            if player.collision_check(asteroid):
                print("Game over!")
                sys.exit()
        pygame.display.flip()
        dt = clock.tick(60)/1000
        
if __name__ == "__main__":
    main()
