import random

from euclideanAlgorithm import euclidean
from fastModularExponentiation import fastModular
from millerRabinPrimalityTest import millerRabin
from chineseRemainderAlgorithm import chineseRemainder


def rsa():
    try:
        def primeGenerator():
            while True:
                num = random.randrange(10000, 100000)
                if millerRabin(num):
                    return num

        p = primeGenerator()
        q = primeGenerator()
        while p == q:
            q = primeGenerator()

        n = p * q
        fin = (p - 1) * (q - 1)

        def relativePrime(fn):
            while True:
                randE = random.randrange(2, fn)
                GCD, x, cd = euclidean(fn, randE)
                if GCD == 1:
                    return randE, cd

        e, d = relativePrime(fin)
        if d < 0:
            d += fin

        return p, q, n, fin, e, d
    except Exception as ex:
        print(f"An error occurred during RSA key generation: {ex}")
        raise


def encrypt(m, e, n):
    try:
        return fastModular(m, e, n)
    except Exception as ex:
        print(f"An error occurred during encryption: {ex}")
        raise


def decrypt(c, d, p, q):
    try:
        return chineseRemainder(c, d, p, q)
    except Exception as ex:
        print(f"An error occurred during decryption: {ex}")
        raise


def signature(m, d, n):
    try:
        return fastModular(m, d, n)
    except Exception as ex:
        print(f"An error occurred during signature generation: {ex}")
        raise


def verify(s, e, p, q):
    try:
        return chineseRemainder(s, e, p, q)
    except Exception as ex:
        print(f"An error occurred during signature verification: {ex}")
        raise


def main():
    try:
        p, q, n, fin, e, d = rsa()
        print(f"p: {p}, q: {q}, n: {n}, fin: {fin}, e: {e}, d: {d}", "\n")

        m = int(input("Enter the message you want to encrypt: "))
        c = encrypt(m, e, n)
        print(f"Encrypted message: {c}")

        decrypted = decrypt(c, d, p, q)
        print(f"Decrypted message: {decrypted}")

        if m == decrypted:
            print("Correct decryption.", "\n")
        else:
            print("Error with decryption!", "\n")

        S = signature(m, d, n)
        print(f"RSA signature: {S}")

        check = verify(S, e, p, q)
        if check == m:
            print(f"Authentic signature")
        else:
            print(f"Error with verification!")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")


if __name__ == '__main__':
    main()
