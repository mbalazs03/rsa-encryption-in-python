from fastModularExponentiation import fastModular
from euclideanAlgorithm import euclidean


def chineseRemainder(c, d, p, q):
    M = p * q
    c1 = fastModular(c, d % (p - 1), p)
    c2 = fastModular(c, d % (q - 1), q)

    _, y1, y2 = euclidean(p, q)

    m = (c1 * y2 * q + c2 * y1 * p) % M
    return m


def main():
    print(chineseRemainder(97, 315, 23, 17))


if __name__ == '__main__':
    main()
