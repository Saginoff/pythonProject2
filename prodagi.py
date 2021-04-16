data = open('input.txt', mode='r', encoding='utf8')
d = dict()
for line in data:
    line = line.strip()
    name = line[:line.find(' ')]
    tovar = line[line.find(' ') + 1:line.rfind(' ')]
    kolvo = int(line[line.rfind(' ') + 1:])
    d[name] = d.setdefault(name, dict())
    d[name][tovar] = d[name].setdefault(tovar, 0) + kolvo
for i in sorted(d):
    print(i + ':')
    [print(j, d[i][j]) for j in sorted(d[i])]
