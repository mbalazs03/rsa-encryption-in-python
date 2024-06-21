def euclidean(a, b):
    x0 = 1
    x1 = 0
    y0 = 0
    y1 = 1
    s = 1

    while b != 0:
        rk = a % b
        qk = a // b
        a = b
        b = rk
        xk = x1
        yk = y1
        x1 = qk * x1 + x0
        y1 = qk * y1 + y0
        x0 = xk
        y0 = yk
        s = -s

    x = s * x0
    y = -s * y0
    (d, x, y) = (a, x, y)
    return d, x, y


def main():
    print(euclidean(220, 27))


if __name__ == "__main__":
    main()
