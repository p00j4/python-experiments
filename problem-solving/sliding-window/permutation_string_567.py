from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        """
        Intution - only small case letters? best to do with 26 char map other wise with dictionary
        slide from left, slide from right
        since it's contiguous characetrs so whole window will slide together so pre load and then remove one from left and add 1 from right into the map
        """
        
        
        n1 = len(s1)
        n2 = len(s2)
        
        if not s1 or not s2 or n1 > n2:
            return False
        s1_ls = [0]*26
        s2_ls = [0]*26
        a = ord('a')
        
        #pre load till s1 length items
        for i, c in enumerate(s1):
            s1_ls[ord(c) - a] += 1
            s2_ls[ord(s2[i]) - a] += 1
        
        left = 0
        for right in range(n1, n2) :
            if s1_ls == s2_ls:
                return True
            
            s2_ls[ord(s2[left]) - a] -= 1   #contract: remove from left
            s2_ls[ord(s2[right]) - a] += 1  #expand: add in right
            left += 1
             
        return s1_ls == s2_ls
        
        
        ### Soulution 1
        n_s1 = len(s1)
        n_s2 = len(s2)
        window_desired = Counter(s1)
        window_cur = Counter(s2[:n_s1])

        left = 0
        right = n_s1
        if window_cur == window_desired:
            return True
        for right in range(n_s1, n_s2): #right movement is controlled here
            #Slide from left - remove left 
            window_cur[s2[left]] -= 1
            if window_cur[s2[left]] == 0:
                del window_cur[s2[left]]
            left += 1

            #Slide to right 
            window_cur[s2[right]] = window_cur.get(s2[right], 0) + 1

            if window_cur == window_desired:
                print("found at {}-{}".format(left, right))
                return True
                
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
            
                
        
            
        
        
        
        
