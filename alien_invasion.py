"""alien_invasion.py        Mathew Peters       Using in class, and repo code, to alter the orientation
 of the spaceship entity while using "W" and "S" keys to move"""

import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    def __init__(self):
        pygame.init()      

        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.settings.dimensions)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

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
        self.aliens.draw(self.screen)

        pygame.display.flip()


    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
              
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _delete_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.left >= 1200:
                self.bullets.remove(bullet)


    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the row"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)


    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("Ship hit!!!")


    def _update_bullets(self):
        self.bullets.update()
        self._delete_bullets()
        self._check_bullet_alien_collisions()


    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)  
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()


    def _update_ship(self):
        self.ship.update()


    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self):
        """Drop the entire dleet and change its direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _create_fleet(self):
        """Create the fleet of alien ships."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - (2 * alien_width)):
                self._create_alien(current_x, current_y)
                current_x += (2 * alien_width)

            current_x = alien_width
            current_y += (2 * alien_height)


    def run_game(self):
        while True:

            self._check_events()

            self.clock.tick(self.settings.clock_tick)
            self._update_ship()
            self._update_bullets()
            self._update_aliens()
            self._delete_bullets()
            self._check_fleet_edges()
            self._update_screen()


if __name__ =='__main__':
    ai = AlienInvasion()
    ai.run_game()

