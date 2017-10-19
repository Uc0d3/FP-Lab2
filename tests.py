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


def run_tests():
    is_prime_test()
    gen_prime_bigger_test()
