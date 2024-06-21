def fastModular(alap, exp, mod):
    bit = []
    while exp != 0:
        bit += str(exp % 2)
        exp = exp // 2
    bit = list(bit)
    bit.reverse()
    bitlen = len(bit)

    for i in range(bitlen):
        bit[i] = int(bit[i])

    prod = 1
    basicpwr = (alap ** (2 ** 0)) % mod
    powers = []
    powers.append(basicpwr)
    for i in range(len(bit) - 1):
        powers.append((basicpwr * basicpwr) % mod)
        basicpwr = (basicpwr * basicpwr) % mod

    powers.reverse()
    b, h = bit, powers

    for i in range(0, len(powers)):
        if b[i] == 1:
            prod *= (h[i])

    return prod % mod


def main():
    print(fastModular(97, 17, 319))


if __name__ == '__main__':
    main()
