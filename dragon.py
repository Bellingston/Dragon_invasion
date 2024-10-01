import pygame


class Dragon():
    '''Класс управления драконом'''

    def __init__(self, di_game) -> None:
        self.screen = di_game.screen
        self.settings = di_game.settings
        self.screen_rect = di_game.screen.get_rect()

        self.image = pygame.image.load('images/dragon.bmp')
        self.image = pygame.transform.scale(self.image, (200, 220))

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.dragon_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.dragon_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.dragon_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.dragon_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
