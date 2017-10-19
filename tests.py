from Functions import *


def is_prime_test():
    assert is_prime(2) is True
    assert is_prime(1) is False
    assert is_prime(13) is True
    assert is_prime(7) is True
    assert is_prime(23) is True
    assert is_prime(0) is False
    assert is_prime(22) is False
    assert is_prime(-1) is False
    assert is_prime(-21) is False
    print ("Is prime test passed")


def gen_prime_bigger_test():
    assert gen_prime_bigger(0) == 2
    assert gen_prime_bigger(1) == 2
    assert gen_prime_bigger(-10) == 2
    assert gen_prime_bigger(7) == 11
    print ("Gen prime bigger test passed")


def year_to_days_test():
    assert year_to_days(0) == 0
    assert year_to_days(-1) is False
    assert year_to_days(1) == 365
    assert year_to_days(4) == 1461
    print("Years to days test passed")


def prime_sibling_test():
    assert prime_sibling(10) == (11, 13)
    assert prime_sibling(1) != (5, 7)
    assert prime_sibling(4) == (5, 7)
    assert prime_sibling(-10) == (3, 5)
    print("Prime Sibling test passed")


def get_dividers_test():
    assert get_dividers(10) == [1, 2, 5]
    assert get_dividers(8) == [1, 2, 4]
    assert get_dividers(8) != [1, 2, 4, 8]
    assert get_dividers(12) == [1, 2, 3, 4, 6]
    assert get_dividers(19) == [1]
    assert get_dividers(-10) == []
    print("Get dividers test passed")


def run_tests():
    is_prime_test()
    gen_prime_bigger_test()
    year_to_days_test()
    prime_sibling_test()
    get_dividers_test()
