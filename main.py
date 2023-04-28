import pygame
import constants as const
import player
import update
from constants import WIDTH
from player import walk_right, walk_left, idle_player


clock = pygame.time.Clock()
bg = pygame.image.load('backgrounds/background_moon.jpg')


def main():
    walk_count = 0
    pygame.init()
    screen = pygame.display.set_mode([const.WIDTH, const.HEIGHT])
    pygame.display.set_caption('MyFirstGame')

# Main Cycle---------------------------------------------------|
    while True:
        keys = pygame.key.get_pressed()

# Walk---------------------------------------------------------|
        if keys[pygame.K_a] and player.player_x > 20:
            player.player_x -= const.SPEED_PLAYER
        elif keys[pygame.K_d] and player.player_x < WIDTH - 100:
            player.player_x += const.SPEED_PLAYER
        walk_count += 1
        if walk_count == len(walk_right):
            walk_count = 0

# Jump---------------------------------------------------------|
        if not player.is_Jump:
            if keys[pygame.K_SPACE]:
                player.is_Jump = True
        else:
            if player.jump_count >= -10:
                if player.jump_count > 0:
                    player.player_y += player.jump_count ** 2 / 3
                else:
                    player.player_y -= player.jump_count ** 2 / 3
                player.jump_count -= 1

            else:
                player.is_Jump = False
                player.jump_count = 10

# Update-------------------------------------------------------|
        update.events()
        update.update(screen, clock, bg, walk_right, walk_left,
                      idle_player, walk_count, player.player_x,
                      player.player_y, keys)


if __name__ == '__main__':
    main()
