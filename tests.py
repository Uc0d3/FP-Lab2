from Functions import *



def is_prime_test():
    assert is_prime(1) is True
    assert is_prime(13) is True
    assert is_prime(7) is True
    assert is_prime(23) is True
    assert is_prime(0) is False
    assert is_prime(22) is False
    assert is_prime(-1) is False
    assert is_prime(-21) is False
    print ("Is prime test passed")


def run_tests():
    is_prime_test()
