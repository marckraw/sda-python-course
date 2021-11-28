import string
# szyfrowanie cezara, przesuniecie o pewna ilosc znakow
# K -> N (przesuniecie o 3)

text = input("Zaszyfruj text: ")



cipher_key = 3

## Cipher
letters_dict = { ord(k): ord(k) + cipher_key for k in string.ascii_letters }

ciphered = text.translate(letters_dict)
print(ciphered)



## Decipher
decipher_letters_dict = { ord(k): ord(k) - cipher_key for k in string.ascii_letters }

deciphered = ciphered.translate(decipher_letters_dict)
print(deciphered)