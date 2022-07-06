import pygame


class Enemy(pygame.sprite.Sprite):
    '''класс ОДНОГО врага'''

    def __init__(self, screen):
        '''инициализируем и задаем начальную позицию врага'''
        super(Enemy, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/z_tank_2.png')
        '''преобразовываем в прямоугольник'''
        self.rect = self.image.get_rect()
        '''помещаем в верхний левый угол экрана'''
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        '''получаем координаты x, y'''
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        '''рисуем врага на экране'''
        self.screen.blit(self.image, self.rect)

    def update(self):
        '''обновляем позицию врага'''
        self.y += 0.1
        self.rect.y = self.y
