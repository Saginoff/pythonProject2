def merge(a:list, b:list):

    c = [0] * (len(a) + len(b))
    ''' функция для сортировки слиянием двух отсортированных списков в один без рекурсии'''
    ''' третий список куда отправляются наименшие из двух списков'''
    i = k = n = 0
    while i < len(a) and k < len(b):
        if a[i] <= b[k]:
            ''' сортировка называется устойчивой если, она не меняет порядок равных элементов'''
            c[n] = a[i]
            i += 1
            n += 1
        else:
            c[n] = b[k]
            k += 1
            n += 1
    while i < len(a):
        '''доливаем из списка оставшиеся элементы'''
        c[n] = a[i]
        i += 1
        n += 1
    while k < len(b):
        c[n] = b[k]
        k += 1
        n += 1
    return c

''' РЕКУРСИВНАЯ ФУНКЦИЯ СОРТИРОВКИ'''

def merge_sort(A):

    if len(A) <= 1:
        '''крайний случай'''
        return
    middle = len(A)//2
    '''делим массив пополам'''
    L = [A[i] for i in range(0, middle)]
    R = [A[i] for  i in range(middle, len(A))]
    merge_sort(L)
    merge_sort(R)
    C = merge(L, R)
    '''вызвается функция сортировки слиянием двух отсортированных списков'''
    for i in range(len(A)):
        A[i] = C[i]


   '''СОРТИРОВКА ТОНИ ХОАРА QuickSort'''
def hoar_sort(A):
    if len(A) <= 1:
        return
    '''крайний случай уже сортировать нечего'''
    barrier = A[0]
    L = []
    M = []
    R = []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R. append(x)

    ''' САМА РЕКУРСИЯ '''
    hoar_sort(L)
    hoar_sort(R)

    '''слив в один список из 3-х'''
    k = 0
    for x in L + M + R:
        A[k] = x
        k += 1



''' ПРОВЕРКА - ОТСОРТИРОВАН ЛИ СПИСОК'''
def check_sorted(A, ascending = True):
    flag = True
    s = 2 * int(ascending) - 1
    '''int(True) = 1 -> +1
       int(False) = 0 -> -1
       s = 2 * x(1 or 0) - 1
       '''
    for i in range(0, len(A) - 1):
        if s * A[i] > s * A[i + 1]:
            flag = False
            break
    return flag




