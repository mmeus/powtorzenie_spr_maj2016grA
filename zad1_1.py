def przestaw(A, n):
    klucz = A[0]
    w = 0
    for k in range(1, n):
        if A[k] < klucz:
            A[w], A[k] = A[k], A[w]
            w += 1
        print(A)

A = [4, 7, 1, 3, 2, 5, 6]
n = len(A)
przestaw(A, n)