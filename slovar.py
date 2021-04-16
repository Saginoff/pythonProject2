'''Требуется составить латино-английский словарь и вывести его в том же виде.
Все слова должны быть упорядочены по алфавиту.
Возможные переводы одного слова должны быть также упорядочены по алфавиту.'''
n = int(input())
'''3
apple - malum, pomum, popula
fruit - baca, bacca, popum
punishment - malum, multa'''
latinEnglish = {}
for i in range(n):
    line = input()
    english = line[:line.find('-')].strip() #разрежем каждую строку на английское и латинские слова
    latinsStr = line[line.find('-') + 1:].strip()
    latins = map(lambda s : s.strip(), latinsStr.split(','))
    print(latins)
    for latin in latins:
        if latin not in latinEnglish: #Каждое из латинских слов возьмем в качестве ключа
            # и добавим к его значениям английское слово (переводов может быть несколько)
            latinEnglish[latin] = []
        latinEnglish[latin].append(english)
print(len(latinEnglish))
for latin in sorted(latinEnglish): #Затем пройдем по сортированным ключам
    # и для каждого ключа выведем отсортированный список переводов
    print(latin, '-', ', '.join(sorted(latinEnglish[latin])))

'''Вывод должен выглядеть так:
7
baca - fruit
bacca - fruit
malum - apple, punishment
multa - punishment
pomum - apple
popula - apple
popum - fruit'''
