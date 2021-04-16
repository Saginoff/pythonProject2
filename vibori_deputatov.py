data = open('input.txt', mode='r', encoding='utf8')
s = dict()
temp = dict()
allVotes = 0
allplace = 450
for line in data:
    line = line.strip()
    party = line[:line.rfind(' ')]
    votes = int(line[line.rfind(' ') + 1:])
    s[party] = votes
felix = sum(s.values()) / 450
for i in s:
    temp[i] = int(s[i] / felix)
allplace -= sum(temp.values())
for i in s:
    temp[i] = [int(s[i] / felix), (s[i] / felix) - int(s[i] / felix)]
listtemp = sorted(temp.items(), key=lambda x: (x[1][1], x[1][0]), reverse=True)
for i in range(allplace):
    listtemp[i][1][0] += 1
temp = dict(listtemp)
for i in s:
    print(i, temp[i][0])
