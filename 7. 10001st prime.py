import math

def eratosthenes(n):
    multiples = []
    primes = []
    for i in range(2, n + 1):
        if i not in multiples:
            primes.append(i)
            if len(primes) == 10001:
                return primes
            else:
                print(len(primes))
            for j in range(i * i, n + 1, i):
                multiples.append(j)

    return primes

if __name__ == "__main__":
    print(eratosthenes(150000))