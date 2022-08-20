import string
import itertools

# generate the lower case english letter


def letters():
    for c in string.ascii_lowercase:
        yield c


for letter in letters():
    print(letter)


def prime_numbers(n):

    prime_cache = set()

    # add the first prime number
    prime_cache.add(2)

    # range includes odd numbers only as even numbers are not prime
    for i in range(3, n, 2):
        is_prime = True
        for j in range(2, i):
            if (i % j) == 0:
                is_prime = False
                break

        if is_prime:
            prime_cache.add(i)
    return prime_cache


def prime_numbers_with_generators(n):

    # 2 being prime
    yield 2

    # range includes odd numbers only as even numbers are not prime
    for i in range(3, n, 2):
        is_prime = True
        for j in range(2, i):
            if (i % j) == 0:
                is_prime = False
                break

        if is_prime:
            yield i


n = 25
primes = prime_numbers_with_generators(n)  # primes is our generator
for num in primes:
    print(num)

# the generator can be converted to a list then you do loose all advantages that it gives you in terms of performance
primes = prime_numbers_with_generators(n)
print(list(primes))