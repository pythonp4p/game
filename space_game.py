import pygame, controls
from ukrainian_tank import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores


def run():
    pygame.init()

    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Ukranian Tank")
    bg_color = (0, 0, 0)
    '''Создаем объект нашего танка'''
    gun = Gun(screen)
    bullets = Group()
    enemies = Group()
    controls.create_army(screen, enemies)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        controls.events(screen, gun, bullets)
        '''Вызываем функцию которая обновляет позицию нашего танка'''
        if stats.run_game:
            gun.update_tank()
            controls.update(bg_color, screen, stats, sc, gun, enemies, bullets)
            controls.update_bullets(screen, stats, sc, enemies, bullets)
            controls.update_enemies(stats, screen, sc, gun, enemies, bullets)


if __name__ == "__main__":
    run()
