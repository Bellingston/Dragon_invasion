import sys
import pygame

from settings import Settings
from dragon import Dragon


class DragonInvasion:
    '''Класс управления игрой'''
    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            # (self.settings.screen_width, self.settings.screen_height)
            (0, 0), pygame.FULLSCREEN
        )
        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width
        pygame.display.set_caption('Dragon Invasion')
        self.dragon = Dragon(self)

    def run_game(self):
        '''Запуск цикла игры'''
        while True:
            self._check_events()
            self.dragon.update()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.dragon.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.dragon.moving_left = True
        elif event.key == pygame.K_UP:
            self.dragon.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.dragon.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.dragon.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.dragon.moving_left = False
        elif event.key == pygame.K_UP:
            self.dragon.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.dragon.moving_down = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.dragon.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    di = DragonInvasion()
    di.run_game()








# def run_game():
#     pygame.init()
#     game_settings = Settings()
#     screen = pygame.display.set_mode(
#         (game_settings.screen_width, game_settings.screen_height)
#         )
#     pygame.display.set_caption("Dragon Invasion")

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
        
#         screen.fill(game_settings.bg_color)

#         pygame.display.flip()

# run_game()
