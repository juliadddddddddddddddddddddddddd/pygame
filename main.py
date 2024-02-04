import pygame
import sys
import os

GRAVITY = 0.045
FPS = 50
pygame.mixer.pre_init(44100, -16, 1, 512)

pygame.init()
pygame.display.set_caption('Приложение для развития навыков при подготовке к ЕГЭ по информатике')
s = pygame.mixer.Sound('data/sounds/звук_нажатия_на_кнопку.ogg')
star = pygame.mixer.Sound('data/sounds/zvuk3.wav')
pygame.mixer.music.load('data/sounds/музыка_на_фон.mp3')
pygame.mixer.music.set_volume(0.5)
font_name = 'data/Gilroy-ExtraBold.otf'
width = 750
height = 750
screen = pygame.display.set_mode((width, height))
BLACK = (11, 76, 87)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
VIOLET = (105, 0, 198)
ORANGE = (255, 102, 0)
WHITE = (255, 255, 255)
COLORS = [RED, YELLOW, GREEN, BLUE, VIOLET, ORANGE]
COLOR_WORD = ['КРАСНЫЙ', 'ЖЕЛТЫЙ', 'ЗЕЛЕНЫЙ', 'СИНИЙ', 'ФИОЛЕТОВЫЙ', 'ОРАНЖЕВЫЙ']

def terminate():
    pygame.quit()
    sys.exit()


def load_image(name, colorkey=None):
    fullname = os.path.join('data/pic', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


screen_rect = (0, 0, width, height)


class Button(pygame.sprite.Sprite):
    def __init__(self, pos, flag=False, touch=False, *args):
        super().__init__()
        if args:
            for i, j in args:
                self.h = i
                self.w = j
        else:
            self.h = 95
            self.w = 375
        self.x, self.y = pos
        image = load_image("кнопка1.png", (255, 255, 255))
        self.image = pygame.transform.scale(image, (self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect_for_text = (self.rect.x + 15, self.rect.y, self.rect.width, self.rect.height)
        self.flag = flag
        self.touch = touch

    def update(self, even_list):
        for event in even_list:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(event.pos):
                s.play()
                self.flag = not self.flag
            elif event.type == pygame.MOUSEMOTION and self.rect.collidepoint(event.pos):
                self.touch = True
            elif event.type == pygame.MOUSEMOTION and not (self.rect.collidepoint(event.pos)):
                self.touch = False


def main():
    from Start_screen import start_screen
    from Main_window import main_window
    all_sprites = pygame.sprite.Group()
    start_screen(screen, all_sprites)
    main_window(screen)
    running = True
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        pygame.display.flip()
        running = False

    pygame.quit()


if __name__ == '__main__':
    main()
