import random
import math

def left_circular_shift(x, n, bit):
    res = ((x << n) & ((1 << bit)-1)) | (x >> (bit-n))
    return res

def right_circular_shift(x, n, bit):
    res = ((x << (bit-n)) & ((1 << bit)-1)) | (x >> n)
    return res


def bit_len(b):
    return (b.bit_length() + 7) // 8 * 8


def is_probable_prime(n, cnt=100): # Miller-Rabin test x cnt
    if n == 2:
        return True
    if n == 1 or n & 1 == 0:
        return False

    U = 278970415063349480483707695 # U=p2*...*p20
    if n >= U and math.gcd(n, U) != 1:
        return False

    d = (n-1) >> 1
    while d & 1 == 0:
        d >>= 1

    for k in range(cnt):
        a = random.randrange(2, n)
        t = d
        y = pow(a, t, n)

        while t != n-1 and y != 1 and y != n-1:
            y = (y * y) % n
            t <<= 1

        if y != n-1 and t & 1 == 0:
            return False

    return True

def gen_prime(bit=2048):
    while True:
        p = random.randrange(1 << (bit-1), 1 << bit)
        if is_probable_prime(p):
            return p


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


def str_to_bin(s):
    binary = "".join([format(ord(c), "08b") for c in s])
    return int(binary, 2)

def bin_to_str(b):
    binary = b.to_bytes(bit_len(b) // 8, "big")
    return str(binary, encoding="utf-8", errors="replace")
