data = open('input.txt', mode='r', encoding='utf8')
outfile = open('output.txt', mode='w', encoding='utf8')
s = dict()
for line in data:
    line = line.strip()
    s[line] = s.get(line, 0) + 1
k = sum(s.values())
s = sorted(s.items(), key=lambda x: (x[1]), reverse=True)
if s[0][1] >= k//2 + 1:
    print(s[0][0], file=outfile)
else:
    print(s[0][0], s[1][0], sep='\n', file=outfile)
