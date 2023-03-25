import numpy as np
import matplotlib.pyplot as plt
#цвета палитры PICO - 8 в RGB формате
palette = {
    0: [0, 0, 0],  # черный
    1: [29, 43, 83],  # темно-синий
    2: [126, 37, 83],  # темно-пурпурный
    3: [0, 135, 81],  # темно-зеленый
    4: [171, 82, 54],  # коричневый
    5: [95, 87, 79],  # темно-серый
    6: [194, 195, 199],  # светло-серый
    7: [255, 241, 232],  # светло-бежевый
    8: [255, 0, 77],  # ярко-красный
    9: [255, 163, 0],  # оранжевый
    10: [255, 236, 39],  # желтый
    11: [0, 228, 54],  # ярко-зеленый
    12: [41, 173, 255],  # голубой
    13: [131, 118, 156],  # фиолетовый
    14: [255, 119, 168],  # розовый
    15: [255, 204, 170],  # светло-оранжевый
}

#функция генерации случайного спрайта
def random_sprite(size):
    sprite = np.ones((size, size))
    # установка частоты появления одного из 3 цветов( где один из них черный - цвет фона)
    probabilities = [0.2, 0.6, 0.2]  # для 0, 1, 2 соответственно
    # проход по всем пикселям спрайта с помощью двойного цикла for
    for i in range(size):
        for j in range(size):
            # если текущий пиксель находится слева от центра изображения
            if j < size // 2:
                # случайно выбираем цвет из 3 с учетом частоты и располагаем с 2х сторон
                sprite[i, j] = sprite[i, size - 1 - j] = np.random.choice([0, 1, 2], p=probabilities)
            # если же текущий пиксель находится в середине изображения и размер изображения нечетный
            elif j == size // 2 and size % 2 == 1:  # odd case
                # случайно выбираем цвет из 3 с учетом частоты
                sprite[i, j] = np.random.choice([0, 1, 2], p=probabilities)
    return sprite


#функция создания карты спрайтов
def create_map(rows, cols, sprite_size, gap_size=2, margins=2):
    # Высота и ширина карты
    map_height = rows * sprite_size + (rows - 1) * gap_size
    map_width = cols * sprite_size + (cols - 1) * gap_size
    # Общая высота и ширина с учетом отступов и промежутков
    total_height = map_height + 2* margins + gap_size * 2
    total_width = map_width +  2* margins + gap_size * 2
    # Создаем массив пикселей RGB, заполненный единицами
    sprite_map = np.ones((total_height, total_width, 3)) # 3 для RGB каналов
    # Заполняем карту случайными спрайтами
    for i in range(rows):
        for j in range(cols):
            # Генерируем случайный спрайт заданного размера
            sprite = random_sprite(sprite_size)
            # Вычисляем координаты текущего спрайта на карте
            row_start = i * (sprite_size + gap_size) + margins + gap_size
            row_end = row_start + sprite_size
            col_start = j * (sprite_size + gap_size) + margins + gap_size
            col_end = col_start + sprite_size
            # Выбираем два случайных цвета из палитры, отличающихся друг от друга
            while True:
                colors = np.random.choice(list(palette.keys())[1:], size=2, replace=False)
                color1, color2 = palette[colors[0]], palette[colors[1]]
                if not np.array_equal(color1, color2):
                    break

            # Меняем цвета спрайта на выбранные цвета из палитры
            sprite_rgb = np.ones((sprite_size, sprite_size, 3))
            #цикл по каждому пикселю спрайта
            for l in range (sprite_size):
                for m in range(sprite_size):
                    #если черный
                    if sprite[l][m] == 1:
                        sprite_rgb[l][m] =[0, 0, 0]
                    #если цвет 0
                    elif sprite[l][m] == 0:
                        sprite_rgb[l][m] = color1
                    # если цвет 2
                    elif sprite[l][m] == 2:
                        sprite_rgb[l][m] = color2
            # Помещаем созданынй спрайт на карту
            sprite_map[row_start:row_end, col_start:col_end] = sprite_rgb

    sprite_map /= np.max(sprite_map) #нормализацию значений пикселей карты спрайтов
    return sprite_map

#создаем карту спрайтов размером 100 на 200
sprite_map = create_map(10, 20 ,8, gap_size=4,margins=1)
#отображение созданной карты
plt.imshow(sprite_map)
plt.show()