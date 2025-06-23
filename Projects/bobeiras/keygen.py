import string
import random


alfanumericos = string.digits + string.ascii_letters
chars = list(alfanumericos)

key = ''

for i in range(32):
    key += random.choice(chars)

print(key)