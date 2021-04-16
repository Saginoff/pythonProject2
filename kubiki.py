inFile = open('input.txt', 'r', encoding='utf8')
k = list(map(int, inFile.readline().strip().split()))
n = k[0]
m = k[1]
cn = set()
cm = set()
for i in range(n):
    cn.add(int(inFile.readline().strip()))
for f in range(m):
    cm.add(int(inFile.readline().strip()))
print(len(cn & cm))
print(*sorted(cn & cm))
print(len(cn - cm))
print(*sorted(cn - cm))
print(len(cm - cn))
print(*sorted(cm - cn))
