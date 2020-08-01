import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
from template import *
import random


class Vernam:
    def key_gen(self, n):
        key = random.randrange(1 << n)
        return key

    def encrypt(self, m, key):
        c = m ^ key
        return c

    def decrypt(self, c, key):
        m_ = self.encrypt(c, key)
        return m_


def main():
    plain_m = input("input m >> ")
    m= str_to_bin(plain_m)
    n = bit_len(m)

    vernam = Vernam()
    key = vernam.key_gen(n)
    c = vernam.encrypt(m, key)
    m_ = vernam.decrypt(c, key)

    print("key \t : %#x" %(key))
    print("m \t : %#x %s" %(m, bin_to_str(m)))
    print("c \t : %#x %s" %(c, bin_to_str(c)))
    print("m\' \t : %#x %s" %(m_, bin_to_str(m_)))

if __name__ == "__main__":
    main()
