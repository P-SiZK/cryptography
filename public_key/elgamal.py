import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
from template import *
import random
import math

import time

def is_primitive_element(g, p, q): # p=2q+1(q:prime)
    #if g % p == 1:
    #    return False
    if pow(g, 2, p) == 1:
        return False
    if pow(g, q, p) == 1:
        return False
    return True

def key_gen(k=1024):
    while True:
        q = gen_prime(k-1)
        p = 2*q+1
        if is_probable_prime(p):
            break

    while True:
        g = random.randrange(2, p)
        if is_primitive_element(g, p, q):
            break

    x = random.randrange(p-1)
    y = pow(g, x, p)

    return (p, g, y), (x)

def encrypt(m, pk):
    p, g, y = pk

    r = random.randrange(p-1)
    c1 = pow(g, r, p)
    c2 = m * pow(y, r, p) % p

    return (c1, c2)

def decrypt(c, pk, sk):
    c1, c2 = c
    p, g, y = pk
    x = sk

    m_ = c2 * pow(c1, p-1-x, p) % p
    return m_


def main():
    plain_m = input("input m >> ")
    m = str_to_bin(plain_m)

    pk, sk = key_gen()
    c = encrypt(m, pk)
    m_ = decrypt(c, pk, sk)

    print("public key : \n\t p = %d, \n\t g = %d, \n\t y = %d" %(pk[0], pk[1], pk[2]))
    print("secret key : \n\t x = %d" %(sk))
    print("m \t : %d %s" %(m, bin_to_str(m)))
    print("c : \n\t c1 = %d, \n\t c2 = %d" %(c[0], c[1]))
    print("m\' \t : %d %s" %(m_, bin_to_str(m_)))

if __name__ == "__main__":
    main()
