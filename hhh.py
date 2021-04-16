def cumsum_and_erase(A=[], erase=1):
    B = [0] * len(A)
    B[0] = A[0]
    C = []
    for i in range(1, len(A)):
        B[i] = B[i - 1] + A[i]

    for i in B:
        if i == erase:
            B.remove(i)

    return print(B)
cumsum_and_erase([5, 1, 4, 5, 14], 15)
