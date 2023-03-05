from ctypes import c_uint32
def decrypt(v, k):
    v0, v1 = v[0], v[1]
    sum_val, delta_val = 0xC6EF3720, 0x9E3779B9
    k0, k1, k2, k3 = k[0], k[1], k[2], k[3]

    for i in range(32):
        v1 = (v1 - (((v0 << 4 ^ v0 >> 5) + v0) ^ (sum_val + k3) ^ ((v0 << 4 ^ v0 >> 5) + k2)))
        v0 = (v0 - (((v1 << 4 ^ v1 >> 5) + v1) ^ (sum_val + k1) ^ ((v1 << 4 ^ v1 >> 5) + k0)))
        sum_val -= delta_val

    return [v0, v1]


message = [0xE3238557,0x6204A1F8, 0xE6537611, 0x174E5747, 0x5D954DA8, 0x8C2DFE97, 0x2911CB4C, 0x2CB7C66B,0xE7F185A0, 0xC7E3FA40, 0x42419867, 0x374044DF, 0x2519F07D, 0x5A0C24D4, 0xF4A960C5, 0x31159418, 0xF2768EC7, 0xAEAF14CF, 0x071B2C95, 0xC9F22699,0xFFB06F41, 0x2AC90051, 0xA53F035D, 0x830601A7, 0xEB475702, 0x183BAA6F, 0x12626744, 0x9B75A72F,0x8DBFBFEC, 0x73C1A46E, 0xFFB06F41, 0x2AC90051,0x97C5E4E9, 0xB1C26A21, 0xDD4A3463, 0x6B71162F, 0x8C075668, 0x7975D565, 0x6D95A700, 0x7272E637]

key = [0, 4, 5, 1]

decrypted_message = []
for i in range(0, len(message), 2):
    v = [message[i], message[i+1]]
    decrypted_v = decrypt(v, key)
    decrypted_message.extend([decrypted_v[0], decrypted_v[1]])

print(decrypted_message)


