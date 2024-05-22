from ciphers.gen_sentences import sentences
def vigenere_cipher_numeric(text, key):
    key_length = len(key)
    key_as_int = [int(i) for i in key]
    plaintext = text.lower()
    ciphertext = ''
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            shift = key_as_int[i % key_length]
            cipher_char = chr((ord(plaintext[i]) - ord('a') + shift) % 26 + ord('a'))
            ciphertext += str(ord(cipher_char) - ord('a')).zfill(1)  # Convert to 2-digit number
    return ciphertext

# Encrypt the sentences
encrypted_sentences = [vigenere_cipher_numeric(sentence, '16') for sentence in sentences]
