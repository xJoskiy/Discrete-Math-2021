def COM_NN_D(x, y):
    if len(x) > len(y):
        return 1
    elif len(x) < len(y):
        return -1
    else:
        for i, k in zip(x, y):
            if i > k:
                return 1
            elif i < k:
                return -1
    return 0
