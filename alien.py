import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load("Images\\alien.bmp")
        self.corrected_image = pygame.transform.rotate(self.image, self.settings.alien_orientation)
        self.rect = self.corrected_image.get_rect()

        self.rect.x = self.rect.height
        self.rect.y = self.rect.width

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.bottom <= screen_rect.bottom) or (self.rect.top >= 0)

    def update(self):
        """Move the alien to the right."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

