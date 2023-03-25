import numpy as np
import matplotlib.pyplot as plt

#функция генерации случайного спрайта
def random_sprite(size):
    sprite = np.ones((size, size))
    # проход по всем пикселям спрайта с помощью двойного цикла for
    for i in range(size):
        for j in range(size):
            # если текущий пиксель находится слева от центра изображения
            if j < size // 2:
                # случайно выбираем черный или белый для пикселей с 2х сторон
                sprite[i, j] = sprite[i, size - 1 - j] = np.random.randint(0, 2)
            # если же текущий пиксель находится в середине изображения и размер изображения нечетный
            elif j == size // 2 and size % 2 == 1:
                # случайно выбираем черный или белый
                sprite[i, j] = np.random.randint(0, 2)
    return sprite

#функция создания карты спрайтов
def create_map(rows, cols, sprite_size, gap_size=2, margins=2):
    # Высота и ширина карты
    map_height = rows * sprite_size + (rows - 1) * gap_size
    map_width = cols * sprite_size + (cols - 1) * gap_size
    # Общая высота и ширина с учетом отступов и промежутков
    total_height = map_height + 2* margins + gap_size * 2
    total_width = map_width +  2* margins + gap_size * 2
    # Создаем массив пикселей
    sprite_map = np.ones((total_height, total_width))
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
            # Помещаем созданынй спрайт на карту
            sprite_map[row_start:row_end, col_start:col_end] = sprite
    return sprite_map

#создаем карту спрайтов размером 100 на 200
sprite_map = create_map(10, 20 ,5, gap_size=4,margins=1)
#отображение созданной карты
plt.imshow(sprite_map, cmap='Greys')
plt.show()