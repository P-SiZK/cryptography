

def left_circular_shift(x, n, bit):
    res = ((x << n) & ((1 << bit)-1)) | (x >> (bit-n))
    return res

def right_circular_shift(x, n, bit):
    res = ((x << (bit-n)) & ((1 << bit)-1)) | (x >> n)
    return res


def bit_len(b):
    return (b.bit_length() + 7) // 8 * 8


def str_to_bin(s):
    binary = "".join([format(ord(c), "08b") for c in s])
    return int(binary, 2)

def bin_to_str(b):
    binary = b.to_bytes(bit_len(b) // 8, "big")
    return str(binary, encoding="utf-8", errors="replace")
