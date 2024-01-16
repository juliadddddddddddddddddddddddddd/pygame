import sqlite3

import pygame

from main import load_image
from main import width
from main import height
from main import font_name
from main import BLACK
from main import Button
from main import terminate
from main import FPS

def final_window(screen, id):
    clock = pygame.time.Clock()
    con = sqlite3.connect('data/tests/pygamebase.db')
    cur = con.cursor()
    fon = pygame.transform.scale(load_image('когнетивные2.png'),
                                 (width, height))
    font = pygame.font.Font(font_name, 37)
    start1 = font.render(' Начать', True, BLACK)
    start2 = font.render(' Начать', True, BLACK, (179, 233, 230))
    res = font.render('Предыдущие результаты', True, BLACK)
    screen.blit(fon, (0, 0))
    if id == 1:
        results = cur.execute(f"""SELECT time FROM Stroop""").fetchall()
        print(results)
    elif id == 2:
        results = cur.execute(f"""SELECT time FROM Schulte""").fetchall()
    elif id == 3:
        results = cur.execute(f"""SELECT time FROM Cursor""").fetchall()
    else:
        results = cur.execute(f"""SELECT time FROM Table_""").fetchall()

    flag = False
    touch = False
    start_btn = Button((screen.get_width() // 2 - start1.get_width() // 2 - 15, 650), flag, touch,
                       (start1.get_height(), start1.get_width()))
    if len(results) < 11:
        for i in range(len(results), 0, -1):
            f = font.render(results[i - 1][0], True, BLACK)
            screen.blit(f,
                        (screen.get_width() // 2 - f.get_width() // 2, 100 + (50 * i), f.get_height(), f.get_width()))
    else:
        count = 0
        for i in results[-10::]:
            f = font.render(i[0], True, BLACK)
            screen.blit(f, (
                screen.get_width() // 2 - f.get_width() // 2, 150 + (50 * count), f.get_height(), f.get_width()))
            count += 1
    while True:
        even_list = pygame.event.get()
        for event in even_list:
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                start_btn.update(even_list)
                if start_btn.flag:
                    return
            elif event.type == pygame.MOUSEMOTION:
                start_btn.update(even_list)
                pass
        screen.blit(fon, (0, 0))
        screen.blit(res, (screen.get_width() // 2 - res.get_width() // 2, 100, res.get_height(), res.get_width()))
        screen.blit(start1, start_btn.rect_for_text)
        if start_btn.touch:
            screen.blit(start2, start_btn.rect_for_text)
        if len(results) < 11:
            for i in range(len(results), 0, -1):
                f = font.render(results[i - 1][0], True, BLACK)
                screen.blit(f, (
                    screen.get_width() // 2 - f.get_width() // 2, 100 + (50 * i), f.get_height(), f.get_width()))
        else:
            count = 0
            for i in results[-10::]:
                f = font.render(i[0], True, BLACK)
                screen.blit(f, (
                    screen.get_width() // 2 - f.get_width() // 2, 150 + (50 * count), f.get_height(), f.get_width()))
                count += 1

        pygame.display.flip()
        clock.tick(FPS)