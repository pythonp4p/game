import pygame, sys
from bullet import Bullet
from enemies import Enemy
import time
import pygame.font


def events(screen, gun, bullets):
    '''Обработка событий'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                gun.mright = True

            elif event.key == pygame.K_a:
                gun.mleft = True

            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                '''Добавляем новый пулю в группу пуль'''
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.mright = False
            elif event.key == pygame.K_a:
                gun.mleft = False


def update(bg_color, screen, stats, sc, gun, enemies, bullets):
    '''обновление экрана'''
    screen.fill(bg_color)
    '''выводим счет игры'''
    sc.show_score()
    '''Отрисовываем наши пули'''
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    '''Отрисовываем наш танк'''
    gun.output()
    enemies.draw(screen)
    pygame.display.flip()


def update_bullets(screen, stats, sc, enemies, bullets):
    '''Обновляем позицию пуль'''
    bullets.update()
    '''удаляем пулю когда ее низ вышел с экрана, чтобы не забирать память'''
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    '''проверяем попадание пули в врага'''

    collections = pygame.sprite.groupcollide(bullets, enemies, True, True)

    if collections:
        for enemies in collections.values():
            stats.score += 10 * len(enemies)
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_guns()
    '''создаем новую армию если враги уничтожены'''
    if len(enemies) == 0:
        bullets.empty()
        create_army(screen, enemies)


def gun_kill(stats, screen, sc, gun, enemies, bullets):
    '''столкновение пушки и армии'''

    if stats.guns_left > 0:
        stats.guns_left -= 1
        sc.image_guns()
        enemies.empty()
        bullets.empty()
        create_army(screen, enemies)
        gun.create_gun()
        time.sleep(1)

    else:
        stats.run_game = False
        pygame.mouse.set_visible(True)


def update_enemies(stats, screen, sc, gun, enemies, bullets):
    '''Обновляем позицию врагов'''
    enemies.update()
    '''проверяем коллизии между врагом и нашим танком, тоесть перекрили ли они друг друга'''
    if pygame.sprite.spritecollideany(gun, enemies):
        gun_kill(stats, screen, sc, gun, enemies, bullets)
    enemies_check(stats, screen, sc, gun, enemies, bullets)


def enemies_check(stats, screen, sc, gun, enemies, bullets):
    '''Проверяем не вышли ли враги за пределы экрана'''
    screen_rect = screen.get_rect()
    for enemy in enemies.sprites():
        if enemy.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, enemies, bullets)
            break


def create_army(screen, enemies):
    '''Создаем армию врагов'''
    enemy = Enemy(screen)
    enemy_width = enemy.rect.width
    number_of_enemies_x = int((700 - 2 * enemy_width) / enemy_width)
    '''расчитываем сколько линий врагов нужно создать по вертикали'''
    enemy_height = enemy.rect.height
    one_enemy_y = int((800 - 100 - 2 * enemy_height) / enemy_height)
    '''создаем ряды врагов'''
    for row_number in range(one_enemy_y - 1):
        for one_enemy in range(number_of_enemies_x):
            enemy = Enemy(screen)
            enemy.x = enemy_width + (one_enemy * enemy_width)
            enemy.y = enemy_height + (enemy_height * row_number)
            enemy.rect.x = enemy.x
            enemy.rect.y = enemy.rect.height + enemy.rect.height * row_number
            '''добавляем врага в группу врагов'''
            enemies.add(enemy)


def check_high_score(stats, sc):
    '''Проверяем на наилучший счет'''
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('highscore.txt', 'w') as f:
            f.write(str(stats.high_score))
