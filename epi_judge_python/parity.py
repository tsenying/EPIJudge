from test_framework import generic_test

PRECOMPUTED_PARITY=[]
def parity(x):
    # TODO - you fill in here.
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF
    return (PRECOMPUTED_PARITY[x >> (3*MASK_SIZE)] ^
            PRECOMPUTED_PARITY[(x >> (2*MASK_SIZE)) & BIT_MASK] ^
            PRECOMPUTED_PARITY[(x >> MASK_SIZE) & BIT_MASK] ^
            PRECOMPUTED_PARITY[x & BIT_MASK])

# works for 8 bit word e.g. 0x11001010 -> 0
PRECOMPUTED_PARITY=[0,1,1,0]
def parity(x):
    # TODO - you fill in here.
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF
    print(PRECOMPUTED_PARITY[(x >> 6))
    return (PRECOMPUTED_PARITY[(x >> 6)] ^
            PRECOMPUTED_PARITY[(x >> 4) & 0b00000011] ^
            PRECOMPUTED_PARITY[(x >> 2) & 0b00000011] ^
            PRECOMPUTED_PARITY[x & 0b00000011])

if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
