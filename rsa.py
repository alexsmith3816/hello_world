import sys
import random
# added comments
sys.setrecursionlimit(20000) # Allow 20000 levels of recursion

def divisors (n, low, high):
    '''Returns True if n has a divisor in the range from low to high.
    Otherwise returns False.'''
    if low > high:
        return False
    elif n % low == 0: # Is n divisible by low?
        return True
    else:
        return divisors (n , low + 1, high)
		

def isPrime (n):
    '''For any n greater than or equal to 2,
    Returns True if n is prime. False if not.'''
    if divisors (n, 2, n-1):
        return False
    else :
        return True
        
def listPrimes (n, limit):
    '''Returns a list of prime numbers between n and limit.'''
    if n == limit:
        return []
    elif isPrime (n):
        return [n] + listPrimes (n+1, limit)
    else:
        return listPrimes (n+1, limit)
        

        
def sift(toRemove, numList):
    '''Takes a number, toRemove, and a list of numbers, numList.
    Returns the list of those numbers in numList that are not multiples of toRemove.'''

    return filter(lambda x: x % toRemove != 0, numList)

def primeSieve(numberList):
    '''Returns the list of all primes in numberList using a prime sieve algorithm.'''
    if numberList == []:      # if the list is empty,
        return []              # ...we're done
    else:
        if numberList[0] == 1 :
            numberList = numberList[1:]
        prime = numberList[0]  # The first element is prime!
        return [prime] + primeSieve(sift(prime, numberList[1:]))
        
def inverse(e, m):
    '''Returns the inverse of e mod m'''
    return filter(lambda d: e*d % m == 1, range(1, m))[0]

def makeEncoderDecoder():
    '''Returns two functions:  An RSA encryption function
       and an RSA decryption function.'''
    #
    # Choose 2 primes:
    #
    p, q = random.sample(primeSieve(range(2, 10)), 2)
    n = p*q          # compute n
    m = (p-1)*(q-1)  # compute m
    print ("Maximum number that can be encrypted is ", n-1)

    #
    # Choose a random prime for e:
    #
    e = random.choice(primeSieve(range(2, m)))
    if m % e == 0:   # If e divides m, it won't work!
        print ("Please try again")
        return
    else:
        d = inverse(e, m)               # compute d
        encoder = lambda x: (x**e) % n  # encryption function
        decoder = lambda y: (y**d) % n  # decryption function
        return [encoder, decoder]

