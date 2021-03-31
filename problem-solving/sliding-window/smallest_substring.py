import sys
from copy import copy
from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        
        freq_t = Counter(t)
        freq_window = {} #to aquire release in this
        
        desired_count = len(t)
        match_count = 0
        l = r = 0
        n = len(s)
        result = ""
        
        while r < n:
            #f1, f2 = False, False
            #acquire
            while r < n and match_count < desired_count:
                cur_ch = s[r]
                if cur_ch in t:
                    freq_window[cur_ch] = freq_window.get(cur_ch,0) + 1

                    if freq_window[cur_ch] <= freq_t[cur_ch]: #window satisfy  when exact char n thier fre are matched
                        match_count += 1
                
                r += 1 #keep moving until window satisfied
                # f1 = True
                
        
            """ collect ans, release"""
            while l < r and match_count == desired_count:
                start_ch = s[l]
                if start_ch in t:
                    cur_str = s[l: r]
                    if len(result) == 0 or len(cur_str) < len(result):
                        result = cur_str

                    if freq_window.get(start_ch) == 1: #last occurence
                        del freq_window[start_ch] 
                    else:
                        freq_window[start_ch] -= 1

                    if freq_window.get(start_ch, 0) < freq_t.get(start_ch, 0):
                        match_count -= 1
                    
                l += 1 #stop moving r, check FROM l to r if there is any shorter window
                # f2 = True

            # if not f1 or not f2:
            #     break
        return result
    
    
    
    #SOLUTION 2
    
    import collections
    def minWindow(s, t):
        need = collections.Counter(t)            #hash table to store char frequency
        missing = len(t)                         #total number of chars we care
        start, end = 0, 0
        left = 0
        for right, char in enumerate(s, 1):       #index right from 1
            if need[char] > 0:
                missing -= 1                      #1 less missing
            need[char] -= 1                       #adding with negative when not found (reduces efforts of deleting the key)
            if missing == 0:                      #match all chars
                while left < right and need[s[left]] < 0:  #move from left to right for the left which is positive in the hash
                    need[s[left]] += 1            #rebuild the need hash 
                    left += 1                       
                need[s[left]] += 1                #make sure the first appearing char satisfies need[char]>0
                missing += 1                      #we missed this first char, so add missing by 1
                if end == 0 or right-left < end-start:  #update window if smaller than before
                    start, end = left, right
                left += 1                           #update left to start+1 for next window
        return s[start:end]

    

        
