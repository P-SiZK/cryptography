import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
from template import *
from des import key_gen as des_key_gen, encrypt as des_encrypt, decrypt as des_decrypt
import random


def key_gen(option=3): # option 1:1key(DES), 2:2key, 3:3key
    key1 = des_key_gen()
    if option == 1:
        return key1

    key2 = des_key_gen()
    if option == 2:
        return key1, key2

    key3 = des_key_gen()
    return key1, key2, key3

def encrypt(m, key1, key2=None, key3=None):
    if key3 == None:
        key3 = key1
    if key2 == None:
        key2 = key1

    c = des_encrypt(m, key1)
    c = des_decrypt(c, key2)
    c = des_encrypt(c, key3)
    return c

def decrypt(c, key1, key2=None, key3=None):
    if key3 == None:
        key3 = key1
    if key2 == None:
        key2 = key1

    c = des_decrypt(c, key3)
    c = des_encrypt(c, key2)
    m_ = des_decrypt(c, key1)
    return m_


def main():
    plain_m = input("input m >> ")
    m = str_to_bin(plain_m)

    key1, key2, key3 = key_gen()
    c = encrypt(m, key1, key2, key3)
    m_ = decrypt(c, key1, key2, key3)

    print("key1 \t : %#x" %(key1))
    print("key2 \t : %#x" %(key2))
    print("key3 \t : %#x" %(key3))
    print("m \t : %#x %s" %(m, bin_to_str(m)))
    print("c \t : %#x %s" %(c, bin_to_str(c)))
    print("m\' \t : %#x %s" %(m_, bin_to_str(m_)))

if __name__ == "__main__":
    main()
