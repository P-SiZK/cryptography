import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
from template import *
import random
import math

def extended_gcd(m, n): # mu+nv=gcd(m,n)
    r0, r1 = m, n
    u0, u1 = 1, 0
    v0, v1 = 0, 1

    while r1 != 0:
        q = r0 // r1

        r0, r1 = r1, (r0 - q * r1)
        u0, u1 = u1, (u0 - q * u1)
        v0, v1 = v1, (v0 - q * v1)

    return u0, v0, r0


def key_gen(k=2048, e=65537):
    p = gen_prime(k)
    q = gen_prime(k)
    N = p * q
    phiN = (p-1)*(q-1)

    if e == None:
        while True:
            e = random.randrange(2, phiN)
            if math.gcd(phiN, e) == 1:
                break

    _, d, _ = extended_gcd(phiN, e)
    d %= phiN

    return (N, e), d

def encrypt(m, pk):
    N, e = pk
    c = pow(m, e, N)
    return c

def decrypt(c, pk, sk):
    N, _, d = *pk, sk
    m_ = pow(c, d, N)
    return m_


def main():
    plain_m = input("input m >> ")
    m = str_to_bin(plain_m)

    pk, sk = key_gen()
    c = encrypt(m, pk)
    m_ = decrypt(c, pk, sk)

    print("public key \t : N = %d, \n\t\t   e = %d" %(pk[0], pk[1]))
    print("secret key \t : d = %d" %(sk))
    print("m \t : %d %s" %(m, bin_to_str(m)))
    print("c \t : %d %s" %(c, bin_to_str(c)))
    print("m\' \t : %d %s" %(m_, bin_to_str(m_)))

if __name__ == "__main__":
    main()
