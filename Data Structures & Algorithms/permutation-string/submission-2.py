from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        freq1 = {}
        length = len(s1)
        n2 = len(s2)
        # count freq for s1
        for s in s1:
            freq1[s] = freq1.get(s,0)+1
        freq2 = {}
        # count freq for s2 with window = len(s1)
        for s in s2[:length]:
            freq2[s] = freq2.get(s,0)+1
        
        for i in range(n2-length+1):
            if freq1 == freq2:
                return True
            letter = s2[i]
            freq2[letter]-=1
            if freq2[letter]==0:
                del freq2[letter]
            if i+length==n2:
                break
            freq2[s2[i+length]]=freq2.get(s2[i+length],0)+1
            i+=1
        return False

