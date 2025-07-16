"""alien_invasion.py        Mathew Peters       Using in class, and repo code, to alter the orientation
 of the spaceship entity while using "W" and "S" keys to move"""

import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    def __init__(self):
        pygame.init()      

        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.settings.dimensions)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        pygame.display.set_caption("Alien Invasion!")

    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:                 # S key down goes down
                self.ship.moving_down = True
            elif event.key == pygame.K_w:               # W key down goes up
                self.ship.moving_up = True
            elif event.key == pygame.K_SPACE:
                self._fire_bullet()
            elif event.key == pygame.K_q:
                sys.exit()

    def _check_keyup_events(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                self.ship.moving_down = False
            elif event.key == pygame.K_w:
                self.ship.moving_up = False


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()

        pygame.display.flip()


    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
              
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _delete_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.left >= 1200:
                self.bullets.remove(bullet)


    def run_game(self):
        while True:

            self._check_events()

            self.clock.tick(self.settings.clock_tick)
            self.ship.update()
            self.bullets.update()
            self._delete_bullets()
            self._update_screen()


if __name__ =='__main__':
    ai = AlienInvasion()
    ai.run_game()

