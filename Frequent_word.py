words = []
with open('C:/Users/PRADEEP/Documents/asd.txt', "r") as f:
    for line in f:
        words.extend(line.split())

from collections import Counter
counts = Counter(words)
top= counts.most_common(1)
print(top)
