import re

data = []
with open('./input.txt', 'r') as f:
    text = f.readlines()
    for line in text:
        word = line.lower().strip()
        word_stripped = re.sub(r'[^\w]', '', word)
        data.append(word_stripped)

for word in data:
    unique_chars = set(word)
    if word == word[::-1]:
        print('YES,', len(unique_chars))
    else:
        print('NO,', -1)

