from fastModularExponentiation import fastModular


def millerRabin(n):
    if n in (2, 3):
        return True
    if n % 2 == 0 or n <= 1:
        return False

    a = 2
    s = 0
    d = n - 1

    while d % 2 == 0:
        d //= 2
        s += 1

    ad = fastModular(a, d, n)

    if ad == 1 or ad == n - 1:
        return True

    for _ in range(s - 1):
        ad = fastModular(ad, 2, n)
        if ad == n - 1:
            return True

    return False


def main():
    if millerRabin(29):
        print("PRÍM")
    else:
        print("NEM PRÍM")


if __name__ == '__main__':
    main()
