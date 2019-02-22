def sumPrimes(n):
    sum, sieve = 0, [True] * n
    for p in range(2, n):
        if sieve[p]:
            sum += p
            for i in range(p*p, n, p):
                sieve[i] = False
    return sum

if __name__ == "__main__":
    print(sumPrimes(2000000))
    #primes = eratosthenes(20000000)
    #sum = 0
    #for prime in primes:
    #    sum += prime
    #print(sum)