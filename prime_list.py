# Implement prime_list(n).
# Return a list of all prime numbers from 2 to n inclusive.
# A prime number has exactly two positive divisors. 
# Students may need to research a simple primality test or the Sieve of Eratosthenes.



def prime_list(n):
    prime_number = []
    for i in range(2, n+1):
        if is_prime(i) :
            prime_number.append(i)
    return prime_number

def is_prime(n) :
    for i in range(2, n) :
        if n <= 1 :
            return False
        if n % i == 0 :
            return False
    return True
