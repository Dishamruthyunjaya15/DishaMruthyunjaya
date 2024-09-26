# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:12:29 2024

@author: SPURGE
"""

def last_candy_recipient(N, K, A):
    last_child = (A - 1 + K - 1) % N + 1
    return last_child

# Example usage:
N, K, A = map(int, input().strip().split())
print(last_candy_recipient(N, K, A))