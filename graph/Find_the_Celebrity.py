"""
Suppose you are at a party with n people (labeled from 0 to n - 1), and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her, but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n). There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.

 

Example 1:


Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.
"""

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):
#from functools import lru_cache

class Solution(object):
    
    """
    00 01 02
    10 11 12
    20 21 22
    """
    """
    Adding cache doens't help in this bcs we anyway don't find the combo in cache much
    better use logical deduction 
    - if any knows other then that can't be a celeb i.e. celeb has to be the other person
    so why o(n2) on anything related to first person. 
    1. find the candidate 
    2. check if its the celebrity in real
    """
    
    def findCelebrity(self, n):
        cache = {}
        celeb_candidate = 0
        for i in range(n):
            if(knows(celeb_candidate, i)):
                celeb_candidate = i
               
        if self.is_celeb(celeb_candidate, cache, n):
            return celeb_candidate
        return -1
    
    
    def is_celeb(self,i, cache, n):
        for j in range(n):
            if i == j:
                continue
            # if i in cache:
            #     return cache[i]
            if(knows(i, j) or not knows(j, i)):
                #cache[i] = False
                return False
        #cache[i] = True
        return True
