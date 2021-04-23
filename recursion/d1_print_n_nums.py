"""
Day 1 to recursion
Print 1 to n numbers without using a loop
"""

"""
Intution: Recursion is the alternative way to simulate a loop 
Think n -> n-1 -> n-2 .... 1 
- Base
- Hypothesis 
- Decision/Induction
"""
# 1. Print in ascending order
def print_n_nums(n):
  if n == 1:
    print(1)
    return 
  print_n_nums(n - 1)
  print(n) #when it starts returning will keep printing in the ascendind order
  
  
# 2. Print in descending order
def print_n_nums(n):
  print(n)
  if n == 1:
    return 
  print_n_nums(n - 1)
