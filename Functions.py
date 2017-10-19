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
    """Generate a list of primes until n"""
    primes = [num for num in range(1, n) if is_prime(num)]
    """ Go trough the list of primes"""
    for prim1 in primes:
        """Go trough the list of primes a second time"""
        for prim2 in primes[0:len(primes) // 2 + 1]:
            if (prim1 + prim2 == n):
                print("%d + %d = %d" % (prim1, prim2, n))


def year_to_days(years):
    if years < 0:
        return False
    """Calculate number of leap years"""
    leap_years = years // 4
    """Add number of leap years to total days"""
    return (years * 365 + leap_years)


def prime_sibling(n):
    """Generate the next prime number """
    prime_num = gen_prime_bigger(n)
    while True:
        if is_prime(prime_num + 2):
            return [prime_num, prime_num + 2]
        prime_num = gen_prime_bigger(prime_num)


"""Returns a list containing dividers of n"""
def get_dividers(n):
    return [d for d in range(1, (n // 2) + 1) if n % d == 0]


def prod_factor(n):
    dividers = get_dividers(n)
    prod = reduce(operator.mul, dividers)  # Multiply all the dividers in list
    return prod


def calc_palindrom(n):
    """Return reversed number"""
    return(int(str(n)[::-1]))


def is_perfect(n):
    dividers = get_dividers(n)
    if dividers:
        suma = reduce(operator.add, dividers)  # Sum up all the dividers in list
        if suma == n:
            return True
    return False


def bigger_perfect(n):
    n += 1
    while not is_perfect(n):
        n += 1
    return(n)


"""Return smaller prime number than n"""
def smaller_prime(n):
    n -= 1
    while not is_prime(n):
        n -= 1
        if n <= 0:
            return False
    return n

"""
Return smaller perfect number than n
If not found return False
"""
def smaller_perfect(n):
    n += 1
    while not is_perfect(n):
        n -= 1
        if n <= 0:
            return False
    return(n)


"""Calculate greater than n number that is part of fibonacci series"""
def greater_fibo(n):
    f1 = 0
    f2 = 1
    while f2 <= n:
        f1, f2 = f2, f1 + f2
    return f2

"""
Return product of prime numbers from list
Return False if no primes are present in list
"""
def prime_list_product(nums):
    primes = [n for n in nums if is_prime(n)]
    if len(primes) > 0:
        return reduce(operator.mul, primes)
    return False

"""
Return sum of prime numbers from list
Return False if no primes are present in list
"""
def prime_list_sum(nums):
    primes = [n for n in nums if is_prime(n)]
    if len(primes) > 0:
        return reduce(operator.add, primes)
    return False

"""
Return max prime number from list
Return False if no primes are present in list
"""
def max_prime_list(nums):
    primes = [n for n in nums if is_prime(n)]
    if len(primes) > 0:
        return max(primes)
    return False

"""
Return min prime number from list
Return False if no primes are present in list
"""
def min_prime_list(nums):
    primes = [n for n in nums if is_prime(n)]
    if len(primes) > 0:
        return min(primes)
    return False


"""
Return sum of non-prime numbers from list
Return False if no non-prime are present in list
"""
def non_prime_list_sum(nums):
    non_primes = [n for n in nums if is_prime(n) is False]
    if len(non_primes) > 0:
        return reduce(operator.add, non_primes)
    return False
