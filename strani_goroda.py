text = open('input.txt')
q = int(text.readline())
sprav = dict()
for i in range(q):
    line = text.readline().strip()
    country = line[:line.find(' ')]
    citys = line[line.find(' ') + 1:].split()
    for c in citys:
        sprav[c] = country
z = int(text.readline())
for i in range(z):
    zapros = text.readline().strip()
    print(sprav[zapros])

'''n = file.readline().split()
        for j in range(1, len(n)):
            myDict[n[j]] = n[0]
            '''