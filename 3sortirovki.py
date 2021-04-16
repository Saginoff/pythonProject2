def insert_sort(A):
    """ Сортировка вставками """
    n = len(A)
    for top in range(1, n):
        k = top
        while k > 0 and A[k - 1] > A[k]:
            A[k], A[k - 1] = A[k - 1], A[k]
            k -= 1

def choice_sort(A):
    """ Сортировка выбором """
    n = len(A)
    for pos in range(0, n - 1):
        for k in range(pos + 1, n):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]



def bubble_sort(A):
    """ Сортировка методом пузырька """
    n = len(A)
    for bypass in range(1, n):
        for k in range(0, n - bypass):
            if A[k] > A[k + 1]:
                A[k], A[k + 1] = A[k + 1], A[k]

def count_sort(A):
    counter = [0] * max(A)
    for i in A:
        counter[i] += 1
    for k in counter:
        for m in range(k):
            print(m)



def test_sort(sort_algorithm):
    print('тестируем: ', sort_algorithm.__doc__)
    print('testcase #1: ', end='')
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print('OK' if A == A_sorted else 'Fail')

    print('testcase #2: ', end='')
    A = list(range(10, 20)) + list(range(0, 10))
    A_sorted = list(range(20))
    sort_algorithm(A)
    print('OK' if A == A_sorted else 'Fail')

    print('testcase #3: ', end='')
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(A)
    print('OK' if A == A_sorted else 'Fail')


if __name__ == '__main__':
    test_sort(insert_sort)
    test_sort(choice_sort)
    test_sort(bubble_sort)
