#eratosthenes algorithm
def sum_of_primes(limit):
    sieve = [True] * limit
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes

    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit, i):
                sieve[j] = False

    return sum(i for i, is_prime in enumerate(sieve) if is_prime)


print("Sum of primes below 2,000,000 is:", sum_of_primes(2000000))
