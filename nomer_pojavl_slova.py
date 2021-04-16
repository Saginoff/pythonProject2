text = open('input.txt').read().strip().split()
s = dict()
for i in text:
    c = s.get(i, 0)
    print(c, end=' ')
    s[i] = c + 1
