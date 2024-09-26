# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 12:34:27 2024

@author: SPURGE
"""

def count_triplets(arr, n, m):
    unique_triplets = set()  
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] * arr[j] * arr[k] == m:
                    triplet = tuple(sorted([arr[i], arr[j], arr[k]]))
                    unique_triplets.add(triplet)
    
    return len(unique_triplets)

# Input Reading
n = int(input())               
arr = list(map(int, input().split()))  
m = int(input())               

result = count_triplets(arr, n, m)
print(result)