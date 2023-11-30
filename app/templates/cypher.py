def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return -1


def affine_encrypt(plaintext, a, b, m=26):
    ciphertext = ""

    for char in plaintext:
        if char.isalpha():
            x = ord(char.upper()) - 65
            y = (a * x + b) % m
            ciphertext += chr(y + 65)
        else:
            ciphertext += char

    return ciphertext


def affine_decrypt(ciphertext, a, b, m=26):
    a_inv = mod_inverse(a, m)

    if a_inv == -1:
        return "a and m must be coprime for the cipher to work"

    plaintext = ""

    for char in ciphertext:
        if char.isalpha():
            y = ord(char.upper()) - 65
            x = (a_inv * (y - b)) % m
            plaintext += chr(x + 65)
        else:
            plaintext += char

    return plaintext


if __name__ == "__main__":
    i = "uqzk"
    a = affine_decrypt(i, 17, 12, 26)
    print(affine_encrypt("cong",17,12,26))
    print(a)

