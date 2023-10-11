alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    cipher_text = []
    for char in text:
        position = alphabet.index(char) + shift
        cipher_text.append(alphabet[position])
    print("The encoded text is " + ''.join(cipher_text))

def decrypt(text, shift):
    plain_text = []
    for char in text:
        position = alphabet.index(char) - shift
        plain_text.append(alphabet[position])
    print("The decoded text is " + ''.join(plain_text))

if direction == 'encode':
    encrypt(text, shift)

elif direction == 'decode':
    decrypt(text, shift)
