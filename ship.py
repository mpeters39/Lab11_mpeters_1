import pygame

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("Images/ship.bmp")
        self.corrected_image = pygame.transform.rotate(self.image, self.settings.ship_orientation)
        self.rect = self.corrected_image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        self.moving_down = False
        self.moving_up = False

        self.y = float(self.rect.y)
        


    def blitme(self):
        self.screen.blit(self.corrected_image, self.rect)


    def update(self):
        
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.ship_speed
        elif self.moving_up and self.rect.top > 0:
            self.rect.y -= self.settings.ship_speed

        self.y = self.rect.y
        #self.rect.y = self.y