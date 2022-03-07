from collections import Counter

c = Counter([0, 1, 2, 0])
print(c)

for i, count in c.most_common():
    print(i, count)