inFile = open('input.txt', 'r', encoding='utf8')
n, k = map(int, inFile.readline().split())
zab = set()
for i in range(k):
    a, b = map(int, inFile.readline().split())
    for x in range(a, n + 1, b):
        zab.add(x)
vix = set()
for i in range(6, n + 1, 7):
    vix.add(i)
for i in range(7, n + 1, 7):
    vix.add(i)
print(len(zab - vix))
