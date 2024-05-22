import random
encrypted_sentences = []
for _ in range(71):
    digit = random.randint(35, 294)
    line = ''.join(str(random.randint(0, 9)) for _ in range(random.randint(35, 294)))
    encrypted_sentences.append(line)


