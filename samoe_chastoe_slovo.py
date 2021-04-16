data = open('input.txt')
s = dict()
d = dict()
text = data.read().strip().split()
for word in text:
    k = s.get(word, 0)
    s[word] = k + 1
a = max(sorted([i for i, k in s.items()]), key=lambda x: s[x])
print(a)
