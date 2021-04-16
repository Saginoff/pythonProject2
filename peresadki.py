n = list(map(int, (input().split())))
ranges = []
for i in range(1, 4, 2):
    if n[i] < n[i - 1]:
        n[i], n[i - 1] = n[i - 1], n[i]
av1 = set()
av2 = set()
for i in range(n[0], n[1] + 1):
    av1.add(i)
for k in range(n[2], n[3] + 1):
    av2.add(k)
print(len(av1 & av2))
