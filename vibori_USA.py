data = open('input.txt')
s = dict()
for line in data:
    familia = line[:line.find(' ')].strip()
    votes = int(line[line.find(' ') + 1:].strip())
    k = s.get(familia, 0)
    s[familia] = votes + k
for i in sorted(s):
    print(i, s[i])
