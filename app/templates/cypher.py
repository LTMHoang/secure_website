def affine_encrypt(text, key1, key2):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((key1 * (ord(char) - offset) + key2) % 26 + offset)
        elif char.isdigit():
            result += chr((key1 * (ord(char) - 48) + key2) % 10 + 48)
        else:
            result += char
    return result


def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return -1


def affine_decrypt(text, key1, key2):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            inv_key1 = mod_inverse(key1, 26)
            if inv_key1 == -1:
                return "Invalid key"
            result += chr((inv_key1 * (ord(char) - offset - key2)) % 26 + offset)
        elif char.isdigit():
            inv_key1 = mod_inverse(key1, 10)
            if inv_key1 == -1:
                return "Invalid key"
            result += chr((inv_key1 * (ord(char) - 48 - key2)) % 10 + 48)
        else:
            result += char
    return result


if __name__ == "__main__":
    i = "uqzk"
    a = affine_decrypt(i, 17, 12, 26)
    print(affine_encrypt("cong",17,12, 26))
    print(a)

