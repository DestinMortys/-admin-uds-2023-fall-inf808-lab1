import random

def encrypt(clear_text, key):
    cipher_text = ""

    for char in clear_text:
        if 'a' <= char <= 'z':
            encrypted_char = chr(
                ((ord(char) - ord('a') + key) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
            char = char.lower()
            encrypted_char = chr(
                ((ord(char) - ord('a') + key) % 26) + ord('a'))
        else:
            # Caractères non alphabétiques, on les laisse inchangés
            encrypted_char = char
        cipher_text += encrypted_char

    return cipher_text


def decrypt(cipher_text, key):
    clear_text = ""

    for char in cipher_text:
        if 'a' <= char <= 'z':
            decrypted_char = chr(
                ((ord(char) - ord('a') - key) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
            char = char.lower()
            decrypted_char = chr(
                ((ord(char) - ord('a') - key) % 26) + ord('a'))
        else:
            decrypted_char = char
        clear_text += decrypted_char

    return clear_text

clear_text = "Hello, World!"
key = random.randint(1, 25)

encrypted_text = encrypt(clear_text, key)
decrypted_text = decrypt(encrypted_text, key)

# Vérifier que la combinaison decrypt(encrypt(clear_text, key)) retourne clear_text
print("Texte chiffré:", encrypted_text)
print("Texte original:", clear_text)
print("Texte déchiffré après chiffrement et déchiffrement:", decrypted_text)

# End-of-file (EOF)
