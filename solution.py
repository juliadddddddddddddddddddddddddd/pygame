import os
import sys

import pygame
import requests

lon = "37.530887"
lat = "55.703118"
delta = "0.002"

params = {
    "ll": ",".join([lon, lat]),
    "spn": ",".join([delta, delta]),
    "l": "map"
}

map_request = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_request, params=params)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

# Запишем полученное изображение в файл.
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((600, 450))
# Рисуем картинку, загружаемую из только что созданного файла.

while pygame.event.wait().type != pygame.QUIT:
    key = pygame.key.get_pressed()
    if key[pygame.K_DOWN]:
        lat = str(float(lat) - 7)
        response = requests.get(map_request, params=params)
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
        print(lat)
    elif key[pygame.K_UP]:
        lat = str(float(lat) + 7)
        response = requests.get(map_request, params=params)
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
        print(lat)
    elif key[pygame.K_LEFT]:
        lon = str(float(lon) + 7)
        response = requests.get(map_request, params=params)
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
        print(lon)
    elif key[pygame.K_RIGHT]:
        lon = str(float(lon) - 7)
        response = requests.get(map_request, params=params)
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
        print(lon)
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)