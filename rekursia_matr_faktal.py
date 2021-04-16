def matryoshka(n):
    if n == 1:
        print('matreshechka')
    else:
        print('verx matre4shki n=', n)
        matryoshka(n - 1)
        print('niz matreshki n = ', n)

matryoshka(10)


def f(n:int): #факториал n! = (n-1)!*n
    assert n >= 0, 'factorial ne opredelen'
    if n == 0:
        return 1
    return f(n - 1) * n


def gcd(a, b): #Алгоритм Евклида (Наиб Общий Делитель НОД)
               # НОД (а,b) = (b, a % b)
    return a if b == 0 else gcd(b, a % b)


def pow(a: float, n: int): #Бысрое возведение в степень
            # an = an-1 * a, a0 = 1
    if n == 0:
        return 1
    elif n % 2 == 1: # nechetrnaja stepen
        return pow(a, n  - 1) * a
    else:
        pow(a * a, n // 2) # an = (a2)n/2 esli chetnajz stepen
