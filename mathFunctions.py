def gcf(x, y):
    while y > 0:
        x, y = y, abs(x - y)

    return x
