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
        
