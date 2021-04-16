inFile = open('input.txt', 'r', encoding='utf8')
n = int(inFile.readline().strip())
spis = [0] * n
otv2 = set()
for i in range(n):
    w = int(inFile.readline().strip())
    list_lang = set()
    for m in range(w):
        list_lang.add(str(inFile.readline().strip()))
        otv2 |= list_lang
    spis[i] = (list_lang)
otv1 = spis[0]
for i in range(len(spis)):
    otv1 &= spis[i]
print(len(otv1))
for x in list(otv1):
    print(x)
print(len(otv2))
for k in list(otv2):
    print(k)
