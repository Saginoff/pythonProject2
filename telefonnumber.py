def sravnenie(a: str, b: str):
    for k in range(-1, -11, -1):
        if a[k] != b[k]:
            return 'NO'
    return 'YES'


tel = open('input.txt')
numb = tel.readline()
newnumb = []
for i in numb:
    if i.isdigit():
        newnumb.append(i)
if len(newnumb) == 7:
    newnumb = ['495'] + newnumb
newnumb = str(''.join(newnumb))
for line in tel:
    tempnumb = []
    for i in line:
        if i.isdigit():
            tempnumb.append(i)
    if len(tempnumb) == 7:
        tempnumb = ['495'] + tempnumb
    tempnumb = str(''.join((tempnumb)))
    print(sravnenie(newnumb, tempnumb))
