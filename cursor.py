import sqlite3
from random import randint

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
screen.fill((255, 255, 255))
class TextRenderer:
    def __init__(self, screen, font, text, x, y, max_width):
        self.screen = screen
        self.font = font
        self.text = text
        self.x = x
        self.y = y
        self.max_width = max_width

    def render_text(self):
        words = [word.split(' ') for word in self.text.splitlines()]
        space = self.font.size(' ')[0]
        max_width, _ = self.screen.get_size()

        for line in words:
            for word in line:
                word_surface = self.font.render(word, True, (0, 0, 0))
                word_width, word_height = word_surface.get_size()
                if self.x + word_width >= self.max_width:
                    self.x = 10
                    self.y += word_height
                self.screen.blit(word_surface, (self.x, self.y))
                self.x += word_width + space
            self.x = 10
            self.y += word_height

def main():
    font = pygame.font.SysFont('Times New Roman', 30)

    con = sqlite3.connect('tests (2).db')
    cur = con.cursor()
    text = cur.execute(f"""SELECT file_name FROM text WHERE id = {randint(1, 2)}""").fetchone()
    with open(text[0], encoding='utf8') as f:
        text = f.read()
    renderer = TextRenderer(screen, font, text, 10, 10, 790)
    renderer.render_text()
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == "__main__":
    main()