 def get_all_anagram_instances(s, p): 
     ...:     result = [] 
     ...:     s_win = [0]*26 
     ...:     p_win = [0]*26 
     ...:     left = right = 0 
     ...:     for c in p: #PRE OCCUPY  
     ...:         p_win[ord(c) - ord('a')] += 1 
     ...:         s_win[ord(s[right]) - ord('a')] += 1 
     ...:         right += 1 
     ...:          
     ...:     if p_win == s_win: 
     ...:         result.append(left) 
     ...:              
     ...:          
     ...:     for right in range(len(p), len(s)):  
     ...:         s_win[ord(s[left]) - ord('a')] -= 1   #SLIDE FROM LEFT
     ...:         left += 1 
     ...:          
     ...:         s_win[ord(s[right]) - ord('a')] += 1  #SLIDE TO RIGHT
       
     ...:         if p_win == s_win:                    #CHECK if desired window 
     ...:             result.append(left) 
     ...:     return result 
