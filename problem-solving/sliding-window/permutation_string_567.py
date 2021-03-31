from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n1 = len(s1)
        n2 = len(s2)
        
        if not s1 or not s2 or n1 > n2:
            return False
        
        s1_ls = [0]*26
        s2_ls = [0]*26
        a = ord('a')
        for i, c in enumerate(s1):
            s1_ls[ord(c) - a] += 1
            s2_ls[ord(s2[i]) - a] += 1 #pre load till s1 length items
        
        left = 0
        for right in range(n1, n2) :
            if s1_ls == s2_ls:
                return True
            
            s2_ls[ord(s2[left]) - a] -= 1   #contract: remove from left
            s2_ls[ord(s2[right]) - a] += 1  #expand: add in right
            left += 1
             
        return s1_ls == s2_ls
         
        #Solution 2
        left = 0
        s_dict = Counter(s1)
        window = {}
        for right in range(0, n2):
            ch = s2[right]
            window[ch] = window.get(ch, 0) + 1 #keep acquiring
            if right > n1-1: #window len mathcing to s1, remove from left
                ch_left = s2[left]
                window[ch_left] -= 1
                if window[ch_left] == 0:
                    del window[ch_left]
                left += 1
            if s_dict == window: #any point when window chars and freq matches, anagram is found
                return True
        return False
            
                
        
            
        
        
        
        
