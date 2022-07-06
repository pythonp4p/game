import pygame.font
from ukrainian_tank import Gun
from pygame.sprite import Group


class Scores():
    '''вывод игровой инфы'''

    def __init__(self, screen, stats):
        '''инициализируем подсчет очков'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        '''настраиваем шрифт для вывода счета'''
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 36)
        '''отрисовываем шрифт для вывода счета на экране'''
        self.image_score()
        self.image_high_score()
        self.image_guns()

    def image_score(self):
        '''преобразовываем тект счета в графическое изображение'''
        self.score_img = self.font.render(str(self.stats.score), True,
                                          self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        '''отрисовываем счет в правом верхнем углу'''
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def image_high_score(self):
        '''преобразовываем рекорд в графическое изображение'''
        self.high_score_image = self.font.render(str(self.stats.high_score),
                                                 True, self.text_color,
                                                 (0, 0, 0))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20

    def image_guns(self):
        '''количество жизней'''
        self.guns = Group()
        for gun_number in range(self.stats.guns_left):
            gun = Gun(self.screen)
            gun.rect.x = 15 + gun_number * gun.rect.width
            gun.rect.y = 10
            self.guns.add(gun)

    def show_score(self):
        '''отображаем счет на экране'''
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.guns.draw(self.screen)
