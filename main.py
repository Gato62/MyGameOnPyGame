import pygame
import constants as const
from player import Player
import update
from constants import WIDTH, HEIGHT
from player import walk_right, walk_left, idle_player


clock = pygame.time.Clock()
bg = pygame.image.load('backgrounds/background_moon.jpg')
pl = Player()


def main():
    walk_count = 0
    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption('MyFirstGame')

# Main Cycle---------------------------------------------------|
    while True:
        keys = pygame.key.get_pressed()

# Walk---------------------------------------------------------|
        if keys[pygame.K_a] and pl.player_x > 20:
            pl.player_x -= const.SPEED_PLAYER
        elif keys[pygame.K_d] and pl.player_x < WIDTH - 100:
            pl.player_x += const.SPEED_PLAYER
        walk_count += 1
        if walk_count == len(walk_right):
            walk_count = 0

# Jump---------------------------------------------------------|
        if not pl.is_Jump:
            if keys[pygame.K_SPACE]:
                pl.is_Jump = True
        else:
            pl.jump()

# Update-------------------------------------------------------|
        update.events()
        update.update(screen, clock, bg, walk_right, walk_left,
                      idle_player, walk_count, pl.player_x,
                      pl.player_y, keys)


if __name__ == '__main__':
    main()
