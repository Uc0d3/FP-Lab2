from Functions import *
from tests import run_tests

run_tests()


obtiuni = """
1 - Genereaza umratorul numar prim
2 - Goldbach
3 - Determina varsta in functie de zile
4 - Genereaza numere prime gemene
5 - Produsul factorilor lui n
6 - Calculeaza palindromul unui numar
7 - Nr perfect mai mare ca n
8 - Nr prim mai mic ca n
9 - Nr perfect mai mic ca n
10 - Numar din fibonacci mai mare ca n
11 - Produs numere prime din sir
12 - Suma numere prime din sir
13 - Cel mai mare numar prim din  sir
14 - Cel mai mic numar prim din  sir
15 - Sume numere neprime din sir
Obtiune:
"""


def read_numbers():
    numbers = input("Numbers (space separated):").strip()
    numbers = list(map(int, numbers.split(" ")))
    return numbers


while True:
    try:
        op = int(input(obtiuni))
        if op == 1:
            num = int(input("num="))
            next_prime = gen_prime_bigger(num)
            print(next_prime)
        if op == 2:
            num = int(input("num="))
            print_godldbach_conjecture(num)
        if op == 3:
            num = int(input("Years:"))
            days = year_to_days(num)
            if days is False:
                print("Please input valid days")
            else:
                print(days)
        if op == 4:
            num = int(input("num="))
            siblings = prime_sibling(num)
            print(siblings)
        if op == 5:
            num = int(input("num="))
            prod = prod_factor(num)
            print(prod)
        if op == 6:
            num = int(input("num="))
            palindrom = calc_palindrom(num)
            print(palindrom)
        if op == 7:
            num = int(input("num="))
            res = bigger_perfect(num)
            print(res)
        if op == 8:
            num = int(input("num="))
            res = smaller_prime(num)
            if res is not False:
                print(res)
            else:
                print("Nu exista")
        if op == 9:
            num = int(input("num="))
            res = smaller_perfect(num)
            if res is not False:
                print(res)
            else:
                print("Nu exista")
        if op == 10:
            num = int(input("num="))
            res = greater_fibo(num)
            print(res)
        if op == 11:
            nums = read_numbers()
            res = prime_list_product(nums)
            if res is not False:
                print(res)
            else:
                print("Nu exista numere prime")
        if op == 12:
            nums = read_numbers()
            res = prime_list_sum(nums)
            if res is not False:
                print(res)
            else:
                print("Nu exista numere prime")
        if op == 13:
            nums = read_numbers()
            res = max_prime_list(nums)
            if res is not False:
                print(res)
            else:
                print("Nu exista numere prime")
        if op == 14:
            nums = read_numbers()
            res = min_prime_list(nums)
            if res is not False:
                print(res)
            else:
                print("Nu exista numere prime")
        if op == 15:
            nums = read_numbers()
            res = non_prime_list_sum(nums)
            if res is not False:
                print(res)
            else:
                print("Nu exista numere neprime")

    except Exception as e:
        print(e)
