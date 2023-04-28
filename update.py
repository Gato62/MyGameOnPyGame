import sys

import pygame

from constants import HEIGHT


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update(screen, clock, bg, walk_right, walk_left,
           idle_player, walk_count, x, y, keys):
    screen.blit(bg, (0, 0))

# Check player orie-----------------------------------------|
    if keys[pygame.K_a]:
        screen.blit(walk_left[walk_count], (x, HEIGHT - y))
    elif keys[pygame.K_d]:
        screen.blit(walk_right[walk_count], (x, HEIGHT - y))
    else:
        screen.blit(idle_player[0], (x, HEIGHT - y))
    pygame.display.flip()
    clock.tick(24)
