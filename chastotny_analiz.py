data = open('input.txt')
outfile = open('output.txt', mode= 'w', encoding= 'utf8')
s = dict()
for line in data:
    s[line] = s.get(line, 0) + 1
text = data.read().strip().split()
for word in text:
    s[word] = s.get(word, 0) + 1
lister = []
for i in s:
    lister.append((s[i], i))
lister.sort(key=lambda x: (-x[0], x[1]))
for k in range(len(lister)):
    print(lister[k][1])
