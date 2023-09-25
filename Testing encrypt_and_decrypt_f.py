import random


def encrypt(clear_text):
    # Génération aléatoire de la clé dans la plage de 1 à 25 inclus
    cipher_text = ""

    for char in clear_text:
        key = random.randint(1, 25)
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


def decrypt(cipher_text):
    decrypted_text = ""

    for key in range(26):
        decrypted_text = ""
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
            decrypted_text += decrypted_char

        # Vérifier si le texte déchiffré est une option valide
        if decrypted_text.islower():
            clear_text = decrypted_text
            break

    return clear_text

clear_text = "Doué, mais dû"
encrypted_text = encrypt(clear_text)
decrypted_text = decrypt(encrypted_text)

# Vérifier que la combinaison decrypt(encrypt(clear_text, key)) retourne clear_text
print("Texte chiffré:", encrypted_text)
print("Texte original:", clear_text)
print("Texte déchiffré après chiffrement et déchiffrement:", decrypted_text)

# End-of-file (EOF)
