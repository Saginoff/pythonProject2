inFile = open('input.txt', 'r', encoding='utf8')


def lineReader(text):
    list_yes = set()
    z = set()
    n = int(text.readline().strip())
    for i in range(1, n + 1):
        list_yes.add(str(i))
    while z != {'HELP'}:
        z = set(map(str, (text.readline().strip().split())))
        n = text.readline().strip().split()
        if n == ['NO']:
            list_yes -= z
        elif n == ['YES']:
            list_yes &= z
    return sorted(list_yes)


print(*lineReader(inFile))
