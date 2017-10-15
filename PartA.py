import operator
from functools import reduce


def is_prime(n):
    if n <= 0:
        return False
    return all(n % i for i in range(2, n // 2 + 1))


def gen_prime_bigger(n):
    next_num = n + 1
    """While breaks when finding a prime number"""
    while not is_prime(next_num):
        next_num += 1
    """Prime number is retured"""
    return (next_num)


def print_godldbach_conjecture(n):
    if n % 2 != 0:
        print("Numarul nu este par")
        return
    primes = [num for num in range(2, n) if is_prime(num)]
    for i in primes:
        for j in primes[0:len(primes) // 2 + 1]:
            if (i + j == n):
                print("%d + %d = %d" % (i, j, n))


def year_to_days(years):
    leap_years = years // 4
    return (years * 365 + leap_years)


def prime_sibling(n):
    prime_num = gen_prime_bigger(n)
    while True:
        if gen_prime_bigger(prime_num) == prime_num + 2:
            return [prime_num, prime_num + 2]
        prime_num = gen_prime_bigger(prime_num)


def get_dividers(n):
    return [d for d in range(1, (n // 2) + 1) if n % d == 0]


def prod_factor(n):
    dividers = get_dividers(n)
    prod = reduce(operator.mul, dividers)
    return prod


def calc_palindrom(n):
    return(int(str(n)[::-1]))


def is_perfect(n):
    dividers = get_dividers(n)
    if dividers:
        suma = reduce(operator.add, dividers)
        if suma == n:
            return True
    return False


def bigger_perfect(n):
    n += 1
    while not is_perfect(n):
        n += 1
    return(n)


def smaller_prime(n):
    n -= 1
    while not is_prime(n):
        n -= 1
        if n <= 0:
            return False
    return n


def smaller_perfect(n):
    n += 1
    while not is_perfect(n):
        n -= 1
        if n <= 0:
            return False
    return(n)


def greater_fibo(n):
    f1 = 0
    f2 = 1
    while f2 <= n:
        f1, f2 = f2, f1 + f2
    return f2


def prime_list_product(nums):
    primes = [n for n in nums if is_prime(n)]
    if len(primes) > 0:
        return reduce(operator.mul, primes)
    return False


def prime_list_sum(nums):
    primes = [n for n in nums if is_prime(n)]
    if len(primes) > 0:
        return reduce(operator.add, primes)
    return False


def max_prime_list(nums):
    primes = [n for n in nums if is_prime(n)]
    if len(primes) > 0:
        return max(primes)
    return False


def min_prime_list(nums):
    primes = [n for n in nums if is_prime(n)]
    if len(primes) > 0:
        return min(primes)
    return False


def non_prime_list_sum(nums):
    non_primes = [n for n in nums if is_prime(n) is False]
    if len(non_primes) > 0:
        return reduce(operator.add, non_primes)
    return False
