class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        l = 0
        freq_t = {}
        for letter in t:
            freq_t[letter] = freq_t.get(letter,0)+1
        # if freq_t != freq_s extend right, else shrink
        freq_s = {}
        res = (-1,-1)
        max_len = float('inf')
        have, need = 0, len(freq_t)
        for r in range(len(s)):
            if s[r] in freq_t:
                freq_s[s[r]] = freq_s.get(s[r],0)+1
                if s[r] in freq_t and freq_s[s[r]] == freq_t[s[r]]:
                    have+=1
            while have == need:
                if max_len>r-l+1:
                    res = (l,r)
                    max_len=r-l+1
                
                if s[l] in freq_t:
                    if freq_s[s[l]]==freq_t[s[l]]:
                        have-=1
                    freq_s[s[l]]-=1
                l+=1
        l,r = res
        return s[l:r+1]
