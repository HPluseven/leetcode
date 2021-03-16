def f(n):
    width = 1
    for _ in range(1, n):
        width += 2
    ret = [[' ']*width for _ in range((2*n-1))]

    i = j = width // 2
    idx = 0
    while i >= 0 and j <= width:
        ret[idx][i] = '*'
        ret[idx][j] = '*'
        i -= 1
        j += 1
        idx += 1
    i += 2
    j -= 2
    while i != j:
        ret[idx][i] = '*'
        ret[idx][j] = '*'
        i += 1
        j -= 1
        idx += 1
    ret[idx][i] = '*'

    for item in ret:
        print(''.join(item))


f(46)
