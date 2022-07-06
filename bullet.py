import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        '''создаем пулю в по текущей позиции танка'''
        super(Bullet, self).__init__()
        '''подгружаем экран'''
        self.screen = screen
        '''создаем пулю по коорд с шириной и высотой'''
        self.rect = pygame.Rect(0, 0, 5, 12)
        self.color = (255, 255, 255)
        self.speed = 4.5
        '''делаем так, чтобы пуля появлялась в верхней позиции танка'''
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        '''перемещение пули вверх'''

        self.y -= self.speed

        self.rect.y = self.y

    def draw_bullet(self):
        '''рисуем пулю на экране'''
        pygame.draw.rect(self.screen, self.color, self.rect)
