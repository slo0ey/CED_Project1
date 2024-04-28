import numpy
import math


def gen_data(size: int):
    return [numpy.random.randint(0, 2) for i in range(size)]


def convert_to_physics(size: int, data: list[int]):
    return [data[i]*5 for i in range(size)]


def gen_noise(size: int, deviation: float = 1.0) -> list[float]:
    return list(deviation * numpy.random.randn(size))


def apply_noise(size: int, data: list[int], noise: list[float]):
    return [data[i] + noise[i] for i in range(size)]


def gen_rayleigh_distribution(size: int):
    d1 = gen_noise(size)
    d2 = gen_noise(size)
    return [math.sqrt(d1[i]**2 + d2[i]**2) for i in range(size)]


def apply_noise_with_rayleigh(size: int, data: list[int], noise: list[float], rayleigh: list[float]):
    return [data[i]*rayleigh[i] + noise[i] for i in range(size)]


def convert_to_bits(size: int, data: list[float]):
    return [0 if data[i] < 2.5 else 1 for i in range(size)]


def check_error_bits(size: int, b1: list[int], b2: list[int]) -> list[int]:
    return [b1[i] ^ b2[i] for i in range(size)]


def print_list_pretty(data: list, fmt: str = "{:10}"):
    for i in range(5):
        for j in range(6):
            index = i*6+j
            print(fmt.format(data[index]), end='')
        print()
    print()