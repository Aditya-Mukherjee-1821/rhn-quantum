import numpy as np

def bits_needed(n):
    return int(np.ceil(np.log2(n)))

def int_to_bin_list(val, bits):
    return list(map(int, format(val, f'0{bits}b')))

def bin_list_to_int(bin_list):
    return int("".join(map(str, bin_list)), 2)

def make_vars(prefix, bits):
    return [f'{prefix}_b{i}' for i in range(bits)]