# Sieve of Eratosthenes is one of the most efficient ways of generating prime numbers within the given range
# The function of sieveOfEratosthenes returns a list of prime numbers from 0 to n.

import time

def sieveOfEratosthenes(n):

  arr = [True] * (n+1)

  for i in range(2,int(n**0.5)+1):

    if arr[i] == True:
      for j in range(i*i, n+1, i):
        arr[j] = False


  res = []

  for i in range(2, n+1):
    if arr[i]:
      res.append(i)

  return res

n = int(input())

t1 = time.time()
primeList = sieveOfEratosthenes(n)
t2 = time.time()


print('Time Taken : {} seconds'.format(t2-t1))
