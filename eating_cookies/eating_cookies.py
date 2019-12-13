#!/usr/bin/python

import sys
# from functools import lru_cache

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

def eating_cookies(n, cache = {}):
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    elif n in cache:
        return cache[n] 
    else:
        cache[n]= eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
        return cache[n]


#    self.assertEqual(eating_cookies(0), 1)
#     self.assertEqual(eating_cookies(1), 1)
#     self.assertEqual(eating_cookies(2), 2)
#     self.assertEqual(eating_cookies(5), 13)
#     self.assertEqual(eating_cookies(10), 274)

print(eating_cookies(10))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')