# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 12:44:43 2024

@author: SPURGE
"""

def two_sum(nums, target):

  num_to_index = {}
  for i, num in enumerate(nums):
    complement = target - num
    if complement in num_to_index:
      return [num_to_index[complement], i]
    num_to_index[num] = i

  raise ValueError("No two numbers add up to the target sum.")
nums = list(map(int,input().split()))
target = int(input())
indices = two_sum(nums, target)
print(indices)