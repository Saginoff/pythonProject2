def DEPOSIT(name: str, money: int, d: dict):
    d[name] = d.setdefault(name, 0) + money
    return d


def INCOME(d: dict, p: int):
    for i in d:
        if d.get(i) > 0:
            d[i] = d.setdefault(i, 0) + int(d.get(i) / 100 * p)
    return d


def TRANSFER(name: str, name2: str, money: int, d: dict):
    d[name] = d.setdefault(name, 0) - money
    d[name2] = d.setdefault(name2, 0) + money
    return d


def WITHDRAW(d: dict, name: str, money: int):
    d[name] = d.setdefault(name, 0) - money
    return d


def BALANCE(d: dict, name: str):
    if name not in d:
        print('ERROR')
    else:
        print(d.get(name))


data = dict()
text = open('input.txt', mode='r', encoding='UTF8')
for line in text:
    spis = line.strip().split()
    if spis[0] == 'DEPOSIT':
        DEPOSIT(spis[1], int(spis[2]), data)
    elif spis[0] == 'INCOME':
        INCOME(data, int(spis[1]))
    elif spis[0] == 'TRANSFER':
        TRANSFER(spis[1], spis[2], int(spis[3]), data)
    elif spis[0] == 'WITHDRAW':
        WITHDRAW(data, spis[1], int(spis[2]))
    elif spis[0] == 'BALANCE':
        BALANCE(data, spis[1])
