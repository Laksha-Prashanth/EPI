from typing import List
import math

from test_framework import generic_test

def checkPrime(n:int) -> bool:
    for i in range(2,int(math.sqrt(n))):
        if i % n == 0:
            return False
    return True


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    # TODO - you fill in here.
    primes = [True]*(n+1)
    primes[0] = True
    primes[1] = True
    result = []

    for i in range(2,n):
        t = 2
        while (i)*t <= n:
            primes[i*t] = False
            t += 1

    for i in range(2,len(primes)):
        if primes[i]:
            result.append(i)


    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
