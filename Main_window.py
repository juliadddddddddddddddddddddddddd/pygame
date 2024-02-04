import sqlite3

import pygame
from main import load_image
from main import font_name
from main import width
from main import height
from main import BLACK
from main import Button
from main import terminate
from Results import final_window
from main import FPS
from Stroop import Strup
from Schulte import Schulte
from Table import Table
from Cursor import Cursor


def main_window(screen):
    global RET
    clock = pygame.time.Clock()
    screen.fill((255, 255, 255))
    vol = 0.5
    con = sqlite3.connect('data/tests/pygamebase.db')
    cur = con.cursor()

    intro_text = ["Тест Струпа",
                  "Таблицы Шульте",
                  "Клиновидные таблицы",
                  "Курсор"]
    fon = pygame.transform.scale(load_image('когнетивные2.png'),
                                 (width, height))
    screen.blit(fon, (0, 0))
    nota = pygame.transform.scale(load_image('нота.png'),
                                  (45, 45))
    screen.blit(nota, (0, 0))
    font = pygame.font.Font(font_name, 55)
    strup1 = font.render(intro_text[0], True, BLACK)
    schulte1 = font.render(intro_text[1], True, BLACK)
    table1 = font.render(intro_text[2], True, BLACK)
    cursor11 = font.render(intro_text[3], True, BLACK)

    flag = False
    touch = False

    strup = Button((screen.get_width() // 2 - strup1.get_width() // 2, 175), flag, touch,
                   (strup1.get_height(), strup1.get_width()))

    schulte = Button((screen.get_width() // 2 - schulte1.get_width() // 2, 300), flag, touch,
                     (schulte1.get_height(), schulte1.get_width()))

    table = Button((screen.get_width() // 2 - table1.get_width() // 2, 425), flag, touch,
                   (table1.get_height(), table1.get_width()))

    cursor = Button((screen.get_width() // 2 - cursor11.get_width() // 2, 550), flag, touch,
                    (cursor11.get_height(),
                     cursor11.get_width()))

    music = Button((0, 0), flag, touch, (45, 45))
    screen.blit(strup1, strup.rect_for_text)
    screen.blit(schulte1, schulte.rect_for_text)
    screen.blit(table1, table.rect_for_text)
    screen.blit(cursor11, cursor.rect_for_text)
    group = pygame.sprite.Group(strup, schulte, table, cursor)
    while True:

        even_list = pygame.event.get()
        for event in even_list:
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                vol -= 0.1
                pygame.mixer.music.set_volume(vol)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                vol += 0.1
                pygame.mixer.music.set_volume(vol)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                group.update(even_list)
                if strup.flag:
                    time = Strup(screen, final_window(screen, 1))
                    if time:
                        cur.execute(f"""INSERT INTO Stroop(time) VALUES(?)""", (time,))
                        con.commit()
                    strup.flag = False
                elif schulte.flag:
                    time = Schulte(screen, final_window(screen, 2))
                    if time:
                        cur.execute(f"""INSERT INTO Schulte(time) VALUES(?)""", (time,))
                        con.commit()
                    schulte.flag = False
                elif cursor.flag:
                    time = Cursor(screen, final_window(screen, 3))
                    if time:
                        cur.execute(f"""INSERT INTO Cursor(time) VALUES(?)""", (time,))
                        con.commit()
                    cursor.flag = False
                    pygame.mouse.set_visible(True)
                elif table.flag:
                    time = Table(screen, final_window(screen, 4))
                    if time:
                        cur.execute(f"""INSERT INTO Table_(time) VALUES(?)""", (time,))
                        con.commit()
                    table.flag = False
                elif event.type == pygame.MOUSEBUTTONDOWN and music.x <= event.pos[0] <= (
                        music.x + music.w) and music.y <= event.pos[1] <= (
                        music.y + music.h):
                    music.update(even_list)
                    if music.flag:
                        pygame.mixer.music.play(-1)
                    else:
                        pygame.mixer.music.stop()
            elif event.type == pygame.MOUSEMOTION:
                group.update(even_list)
                pass

        screen.blit(fon, (0, 0))
        screen.blit(nota, (0, 0))
        group.draw(screen)
        strup2 = font.render(intro_text[0], True, BLACK, (179, 233, 230))
        schulte2 = font.render(intro_text[1], True, BLACK, (179, 233, 230))
        table2 = font.render(intro_text[2], True, BLACK, (179, 233, 230))
        cursor21 = font.render(intro_text[3], True, BLACK, (179, 233, 230))

        if strup.touch:
            screen.blit(strup2, strup.rect_for_text)
        elif schulte.touch:
            screen.blit(schulte2, schulte.rect_for_text)
        elif cursor.touch:
            screen.blit(cursor21, cursor.rect_for_text)
        elif table.touch:
            screen.blit(table2, table.rect_for_text)

        screen.blit(strup1, strup.rect_for_text)
        screen.blit(schulte1, schulte.rect_for_text)
        screen.blit(table1, table.rect_for_text)
        screen.blit(cursor11, cursor.rect_for_text)
        pygame.display.flip()
        clock.tick(FPS)
