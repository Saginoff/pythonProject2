data = open('input.txt')
q = int(data.readline())
s = dict()
for i in range(q):
    pair = data.readline().strip().split()
    s[pair[0]] = pair[1]
    s[pair[1]] = pair[0]
print(s[data.readline().strip()])
