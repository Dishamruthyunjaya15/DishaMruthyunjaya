# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 12:38:55 2024

@author: SPURGE
"""

def next_prime(N):
  num = N + 1

  
  while True:
    
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
      if num % i == 0:
        is_prime = False
        break

    
    if is_prime:
      return num

    
    num += 1

N = int(input())

result = next_prime(N)


print(result)