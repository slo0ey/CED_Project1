from matplotlib import pyplot

from utils import *
from solution import *


# 레일리 산란 적용x
def test_normal(size: int):
    data = gen_data(size)
    print("== data ==")
    print(data[:30], "\n")


    x = convert_to_physics(size, data)
    print("== x ==")
    print(x[:30], "\n")


    n = gen_noise(size)
    print("== n ==")
    print_list_pretty(n[:30], "{:10.4f}")


    r = apply_noise(size, x, n)
    print("== r ==")
    print_list_pretty(r[:30], "{:10.4f}")


    y = convert_to_bits(size, r)
    print("== y ==")
    print(y[:30], "\n")


    check = check_error_bits(size, data, y)
    print("== check(correct: 0, error: 1) ==")
    print(check[:30], "\n")


    error_bits = sum(check)
    print("correct bits: {}".format(size - error_bits))
    print("error rate: {:.6f}\n".format(error_bits / size))


    error_rate = []
    for deviation in range(30):
        deviation = deviation / 10

        n2 = gen_noise(size, deviation)
        r2 = apply_noise(size, x, n2)
        y2 = convert_to_bits(size, r2)
        check2 = check_error_bits(size, data, y2)
        error_bits2 = sum(check2)
        error_rate.append(error_bits2 / size)

    print("== error_rate ==")
    for i in range(30):
        print("deviation: {:.1f} / error rate: {:.6f}".format(i/10, error_rate[i]))

    pyplot.plot(numpy.arange(0.0, 3.0, 0.1), error_rate, label="normal")
    pyplot.axis((0.0, 3.0, 0.0, 0.3))
    pyplot.show()


# 레일리 산란 적용
def test_rayleigh(size: int):
    data = gen_data(size)
    print("== data ==")
    print(data[:30], "\n")


    x = convert_to_physics(size, data)
    print("== x ==")
    print(x[:30], "\n")


    n = gen_noise(size)
    print("== n ==")
    print_list_pretty(n[:30], "{:10.4f}")


    h = gen_rayleigh_distribution(size)
    print("== h ==")
    print_list_pretty(h[:30], "{:10.4f}")


    r = apply_noise_with_rayleigh(size, x, n, h)
    print("== r ==")
    print_list_pretty(r[:30], "{:10.4f}")


    y = convert_to_bits(size, r)
    print("== y ==")
    print(y[:30], "\n")


    check = check_error_bits(size, data, y)
    print("== check(correct: 0, error: 1) ==")
    print(check[:30], "\n")


    error_bits = sum(check)
    print("correct bits: {}".format(size - error_bits))
    print("error rate: {:.6f}\n".format(error_bits / size))


    error_rate = []
    for deviation in range(30):
        deviation = deviation / 10

        n2 = gen_noise(size, deviation)
        r2 = apply_noise_with_rayleigh(size, x, n2, h)
        y2 = convert_to_bits(size, r2)
        check2 = check_error_bits(size, data, y2)
        error_bits2 = sum(check2)
        error_rate.append(error_bits2 / size)

    print("== error_rate ==")
    for i in range(30):
        print("deviation: {:.1f} / error rate: {:.6f}".format(i/10, error_rate[i]))

    pyplot.plot(numpy.arange(0.0, 3.0, 0.1), error_rate, label="rayleigh")
    pyplot.axis((0.0, 3.0, 0.0, 0.3))
    pyplot.show()


def test_gray_code(size: int):
    data = gen_data(size)
    print("== data ==")
    print(data[:30], "\n")

    gray_code = gen_gray_code(data, size)
    print("== gray_code ==")
    print(gray_code[:30], "\n")