import numpy


def gen_gray_code(data: list[int], size: int) -> list[int]:
    gray_code = numpy.zeros(shape=(size,), dtype=int)
    gray_code[0] = 0 ^ data[0]
    for i in range(1, size):
        gray_code[i] = data[i-1] ^ data[i]

    return list(gray_code)

def fix_bits(data: list[int], gray_code: list[int], size: int) -> list[int]:
    data[0] = 0 ^ gray_code[0]
    for i in range(1, size):
        data[i] = data[i-1] ^ gray_code[i]

