inFile = open('input.txt', 'r', encoding='utf8')


def lineReader(text):
    list_yes = set()
    z = set()
    n = int(text.readline().strip())
    for i in range(1, n + 1):
        list_yes.add(str(i))
    for p in range(n):
        z = set(map(str, (text.readline().strip().split())))
        if z == {'HELP'}:
            return map(int, (list_yes))
        if len(list_yes & z) <= len(list_yes)//2:
            print('NO')
            list_yes -= z
        else:
            print('YES')
            list_yes &= z


print(*sorted(lineReader(inFile)))
