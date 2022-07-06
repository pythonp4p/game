import pygame
from pygame.sprite import Sprite


class Gun(Sprite):

    def __init__(self, screen):
        '''Инициализация укр.танка'''
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('images/ukrainian_tank.png')
        '''Получаем нашу картинку как объект rect в качестве прямоугольника'''
        self.rect = self.image.get_rect()
        '''Получаем объект нашего экрана в качестве прямоугольника'''
        self.screen_rect = screen.get_rect()
        '''Прописываем координаты центра нашего танка'''
        self.rect.centerx = self.screen_rect.centerx

        self.center = float(self.rect.centerx)
        '''Прописываем координаты низа нашего танка'''
        self.rect.bottom = self.screen_rect.bottom

        self.mright = False

        self.mleft = False

    def output(self):
        '''Рисование пушки на экране'''
        self.screen.blit(self.image, self.rect)

    def update_tank(self):
        '''Обновление позиции танка'''

        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 1.5

        if self.mleft and self.rect.left > 0:
            self.center -= 1.5

        self.rect.centerx = self.center

    def create_gun(self):
        '''размещаем пушку на экране по центру и внизу'''
        self.center = float(self.screen_rect.centerx)
