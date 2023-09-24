import secrets
from binascii import hexlify
import textwrap


def freq_text( clear_text_hugo:str )->list:
  freq = {}
  for letter in clear_text_hugo:
        if letter == '\n':
          continue
        if letter in freq:
                freq[letter] += 1
        else:
                freq[letter] = 1
  return sorted(freq.items(), key=lambda item : item[1], reverse=True)


def freq_cipher( cipher_text_1:bytes ) ->list:
  freq = {}
  for index in range(len(cipher_text_1)):
    if index%2 == 0:
            char = cipher_text_1[index:index+2] 
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
  
  return sorted(freq.items(), key=lambda item : item[1], reverse=True)



def guess_clear_text(cipher_text_1:bytes, decryption_key:dict)  -> str:
    clear_text = ""
    for index in range(len(cipher_text_1)):
        if index % 2 == 0:
            char = cipher_text_1[index:index+2]  
            clear_char = decryption_key.get(char, "%s" % char)
            clear_text += clear_char
    return clear_text


def build_decryption_key(freq_clear_text: list, freq_cipher_text: list, key_size: int) -> dict:
    decryption_key = {}
    
    for i in range(min(key_size, len(freq_cipher_text))):
        freq_cipher_char, _ = freq_cipher_text[i]
        freq_clear_char, _ = freq_clear_text[i]
        decryption_key[freq_cipher_char] = freq_clear_char
    return decryption_key

if __name__ == '__main__':
    
    cipher_text_1_path = "cipher_text_1.bin"
    cipher_text_2_path = "cipher_text_2.bin"
    text_hugo_path = "text_hugo.txt"
    
    with open(cipher_text_1_path, 'br') as f:
        cipher_text_1 = f.read()
    with open(cipher_text_2_path, 'br') as f:
        cipher_text_2 = f.read()
    with open(text_hugo_path, 'r') as f:
        clear_text_hugo = f.read()

    # Obtenir les fréquences des caractères pour clear_text_hugo et cipher_text_1
    freq_hugo = freq_text(clear_text_hugo)
    freq_cipher_text_1 = freq_cipher(cipher_text_1)
    

    # Construire une clé de déchiffrement partielle basée sur les caractères les plus fréquents
    decryption_key = build_decryption_key(freq_hugo, freq_cipher_text_1, 15)
    
    # Devinez le texte clair en utilisant la clé de déchiffrement partielle
    clear_text_1 = guess_clear_text(cipher_text_1, decryption_key) 

  
print("*** question 8 " ) 
freq_hugo = freq_text(clear_text_hugo)
print( "freq_hugo: %s"%freq_hugo ) 


print( "*** question 9" )
freq_cipher_text_1 = freq_cipher(cipher_text_1)
print(freq_cipher_text_1)


print( "*** question 11")
print("decryption_key: %s"%decryption_key)
print("clear_text_1: %s"%clear_text_1 )

"""
print( "*** question 12" )
freq_cipher_text_2 = freq_cipher( cipher_text_2 )
decryption_key = build_decryption_key(  freq_hugo, freq_cipher_text_2, key_size=15 )
print("decryption_key: %s"%decryption_key)
clear_text_2 = guess_clear_text( cipher_text_2, decryption_key ) 
print("clear_text_2: %s"%clear_text_2 )
 

print( "*** question 13" )
indice = "Anton Voyl n'arrivait pas à dormir"
  
decryption_key = {}

for index in range(len(indice)):
            bin_char = cipher_text_2[2 * index : 2 * index +  2 ]
            decryption_key[ bin_char ] = indice[ index ]  
  
clear_text_2 = guess_clear_text( cipher_text_2, decryption_key) 
print("clear_text_2: %s"%clear_text_2 )
"""