from faker import Faker
import random

fake = Faker()

sentences = []
while len(sentences) < 71:
    sentence = fake.sentence()
    if 40 <= len(sentence) <= 300:
        sentences.append(sentence)
