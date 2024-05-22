from ciphers.gen_sentences import sentences

def encrypt(message):
    cipher_text = ""
    for char in message:
        if char.isalpha():
            # Convert the character to its corresponding number
            num = ord(char.lower()) - ord('a') + 1
            cipher_text += str(num)
    return cipher_text

# Encrypt the sentences
encrypted_sentences = [encrypt(sentence) for sentence in sentences]
