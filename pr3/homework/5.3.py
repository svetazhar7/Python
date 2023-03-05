#вообще не уверена в реализации потому что расшифровка
#какая-то странная


from ctypes import c_uint32
# импортирование c_uint32, чтобы гарантировать, что они представлены в
# виде 32-битных целых чисел.


def decrypt(v, k):
    v0 = c_uint32(v[0])
    v1 = c_uint32(v[1])
    sum = c_uint32(0xc6ef3720)
    delta = c_uint32(0x9e3779b9)
    for i in range(32):
        v1.value -= (v0.value << 4) + \
            k[2] ^ v0.value + sum.value ^ (v0.value >> 5) + k[3]
        v0.value -= (v1.value << 4) + \
            k[0] ^ v1.value + sum.value ^ (v1.value >> 5) + k[1]
        sum.value -= delta.value

    return [v0.value, v1.value]

key = [0, 4, 5, 1]  # ключ
# данные для декодирования
data = [0xE3238557, 0x6204A1F8, 0xE6537611, 0x174E5747,
        0x5D954DA8, 0x8C2DFE97, 0x2911CB4C, 0x2CB7C66B,
        0xE7F185A0, 0xC7E3FA40, 0x42419867, 0x374044DF,
        0x2519F07D, 0x5A0C24D4, 0xF4A960C5, 0x31159418,
        0xF2768EC7, 0xAEAF14CF, 0x071B2C95, 0xC9F22699,
        0xFFB06F41, 0x2AC90051, 0xA53F035D, 0x830601A7,
        0xEB475702, 0x183BAA6F, 0x12626744, 0x9B75A72F,
        0x8DBFBFEC, 0x73C1A46E, 0xFFB06F41, 0x2AC90051,
        0x97C5E4E9, 0xB1C26A21, 0xDD4A3463, 0x6B71162F,
        0x8C075668, 0x7975D565, 0x6D95A700, 0x7272E637]
result=[]
str=' '
for i in range (0,39,2):
    result.append(decrypt([data[i],data[i+1]], key))

# преобразование чисел в символы Unicode
decoded_text = ""
for pair in result:
    decoded_text += chr(pair[0]) + chr(pair[1])
# вывод звсекреченного сообщения
print(decoded_text)



