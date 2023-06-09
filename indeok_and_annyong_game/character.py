import sys
import pygame
from pygame.locals import *


class Character:
    def __init__(self, location):
        _location = location
        self.rect = pygame.Rect(
            location[0], location[1], self.image.get_width(),
            self.image.get_height())
        # motion
        self.moving_right = False
        self.moving_left = False
        self.jumping = False
        self.y_velocity = 0
        self.air_timer = 0
        # current state
        self._alive = True

    def calc_movement(self):
        """
        Set motion and physics constants and calculate movement
        """
        # Motion constants
        LATERAL_SPEED = 3.9
        JUMP_SPEED = -9.5
        GRAVITY = 0.35
        TERMINAL_VELOCITY = 8

        # set initially to not moving
        self._movement = [0, 0]
        # calculate horizontal movement
        if self.moving_right:
            self._movement[0] += LATERAL_SPEED
        if self.moving_left:
            self._movement[0] -= LATERAL_SPEED

        # calculate vertical movement
        if self.jumping:
            self.y_velocity = JUMP_SPEED
            self.jumping = False
        self._movement[1] += self.y_velocity
        self.y_velocity += GRAVITY
        # establish terminal velocity of 3px/frame
        if self.y_velocity > TERMINAL_VELOCITY:
            self.y_velocity = TERMINAL_VELOCITY

    def kill_player(self):
        """
        Kill the player by setting the alive status of the player to False
        """
        self._alive = False

    def get_movement(self):
        """
        Return a list containing movement of the character
        """
        return self._movement

    def is_dead(self):
        """
        Return a boolean that indicates if the player is alive or dead
        """
        return self._alive is False

    def get_type(self):
        """
        Return string that contains the character type (indeok or annyong)
        """
        return self._type


class Indeok(Character):
    def __init__(self, location):
        self.image = pygame.image.load('resources/player_images/indeok.png')
        self.side_image = pygame.image.load(
            'resources/player_images/indeokside.png')
        self._type = "indeok"
        super().__init__(location)


class Annyong(Character):
    def __init__(self, location):
        self.image = pygame.image.load('resources/player_images/annyong.png')
        self.side_image = pygame.image.load(
            'resources/player_images/annyongside.png')
        self._type = "annyong"
        super().__init__(location)
