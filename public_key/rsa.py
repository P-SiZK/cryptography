import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
from template import *
import random
import math


def key_gen(k=2048, e=65537):
    p = gen_prime(k >> 1)
    q = gen_prime(k >> 1)
    N = p * q
    phiN = (p-1)*(q-1)

    if e == None:
        while True:
            e = random.randrange(2, phiN)
            if math.gcd(phiN, e) == 1:
                break

    d = extended_gcd(phiN, e)[1] % phiN

    return (N, e), (p, q, d)

def encrypt(m, pk):
    N, e = pk
    c = pow(m, e, N)
    return c

def decrypt(c, sk):
    p, q, d = sk
    a = extended_gcd(q, p)[1] % q
    d1, d2 = d % (p-1), d % (q-1)

    c1, c2 = c % p, c % q
    m1, m2 = pow(c1, d1, p), pow(c2, d2, q)
    m_ = (a * (m2 - m1) % q) * p + m1
    return m_


def main():
    plain_m = input("input m >> ")
    m = str_to_bin(plain_m)

    pk, sk = key_gen()
    c = encrypt(m, pk)
    m_ = decrypt(c, sk)

    print("public key : \n\t N = %d, \n\t e = %d" %(pk[0], pk[1]))
    print("secret key : \n\t p = %d, \n\t q = %d, \n\t d = %d" %(sk[0], sk[1], sk[2]))
    print("m \t : %d %s" %(m, bin_to_str(m)))
    print("c \t : %d %s" %(c, bin_to_str(c)))
    print("m\' \t : %d %s" %(m_, bin_to_str(m_)))

if __name__ == "__main__":
    main()
