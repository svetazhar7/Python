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



sprite = random_sprite(5)
plt.imshow(sprite,cmap='Greys')
plt.show()
