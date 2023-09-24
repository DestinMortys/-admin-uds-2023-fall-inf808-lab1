import random
intercepted_message = 'fytgpcdtep op dspcmczzvp'


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
    clear_text = ""

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


def brute_force(intercepted_message):
    brute_force_dict = {}

    for key in range(26):  # Il y a 26 décalages possibles dans l'alphabet
        clear_text = ""
        for char in intercepted_message:
            if char.isalpha():
                if char.isupper():
                    decrypted_char = chr(
                        ((ord(char) - ord('A') - key) % 26) + ord('A'))
                else:
                    decrypted_char = chr(
                        ((ord(char) - ord('a') - key) % 26) + ord('a'))
                clear_text += decrypted_char
            else:
                clear_text += char

        brute_force_dict[key] = clear_text

    return brute_force_dict


# Attaque de force brute
result = brute_force(intercepted_message)

# Affichage des résultats
for key, clear_text in result.items():
    print(f'Clé {key}: {clear_text}')
