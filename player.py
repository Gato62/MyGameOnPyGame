import pygame

# PLayer Animation--------------------------------------------|
walk_right = [
    pygame.image.load('sprites/walk_right/walk_right_1.png'),
    pygame.image.load('sprites/walk_right/walk_right_1.png'),
    pygame.image.load('sprites/walk_right/walk_right_2.png'),
    pygame.image.load('sprites/walk_right/walk_right_2.png'),
    pygame.image.load('sprites/walk_right/walk_right_3.png'),
    pygame.image.load('sprites/walk_right/walk_right_3.png'),
    pygame.image.load('sprites/walk_right/walk_right_4.png'),
    pygame.image.load('sprites/walk_right/walk_right_4.png'),
    pygame.image.load('sprites/walk_right/walk_right_5.png'),
    pygame.image.load('sprites/walk_right/walk_right_5.png'),
    pygame.image.load('sprites/walk_right/walk_right_6.png'),
    pygame.image.load('sprites/walk_right/walk_right_6.png'),
    pygame.image.load('sprites/walk_right/walk_right_7.png'),
    pygame.image.load('sprites/walk_right/walk_right_7.png'),
    pygame.image.load('sprites/walk_right/walk_right_8.png'),
    pygame.image.load('sprites/walk_right/walk_right_8.png'),
    pygame.image.load('sprites/walk_right/walk_right_9.png'),
    pygame.image.load('sprites/walk_right/walk_right_9.png'),
    pygame.image.load('sprites/walk_right/walk_right_10.png'),
    pygame.image.load('sprites/walk_right/walk_right_10.png')
]
walk_left = [
    pygame.image.load('sprites/walk_left/walk_left_1.png'),
    pygame.image.load('sprites/walk_left/walk_left_1.png'),
    pygame.image.load('sprites/walk_left/walk_left_2.png'),
    pygame.image.load('sprites/walk_left/walk_left_2.png'),
    pygame.image.load('sprites/walk_left/walk_left_3.png'),
    pygame.image.load('sprites/walk_left/walk_left_3.png'),
    pygame.image.load('sprites/walk_left/walk_left_4.png'),
    pygame.image.load('sprites/walk_left/walk_left_4.png'),
    pygame.image.load('sprites/walk_left/walk_left_5.png'),
    pygame.image.load('sprites/walk_left/walk_left_5.png'),
    pygame.image.load('sprites/walk_left/walk_left_6.png'),
    pygame.image.load('sprites/walk_left/walk_left_6.png'),
    pygame.image.load('sprites/walk_left/walk_left_7.png'),
    pygame.image.load('sprites/walk_left/walk_left_7.png'),
    pygame.image.load('sprites/walk_left/walk_left_8.png'),
    pygame.image.load('sprites/walk_left/walk_left_8.png'),
    pygame.image.load('sprites/walk_left/walk_left_9.png'),
    pygame.image.load('sprites/walk_left/walk_left_9.png'),
    pygame.image.load('sprites/walk_left/walk_left_10.png'),
    pygame.image.load('sprites/walk_left/walk_left_10.png'),

]
idle_player = [
    pygame.image.load('sprites/idle_player/idle_1.png')
]


class Player():
    def __init__(self):
        self.speed_player = 15
        self.is_jump = False
        self.velocity = 10
        self.jump_count = self.velocity

    # Start position----------------------------------------------|
        self.player_x = 200
        self.player_y = 150

    def jump(self):
        if self.jump_count >= -self.velocity:
            if self.jump_count > 0:
                self.player_y += self.jump_count ** 2 / 2
            else:
                self.player_y -= self.jump_count ** 2 / 2
            self.jump_count -= 1

        else:
            self.is_jump = False
            self.jump_count = self.velocity
