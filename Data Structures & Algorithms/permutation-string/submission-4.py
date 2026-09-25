class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        freq1,freq2 = {},{}
        length = len(s1)
        n2 = len(s2)
        for i in range(len(s1)):
            freq1[s1[i]] = freq1.get(s1[i],0)+1
            freq2[s2[i]] = freq2.get(s2[i],0)+1
        
        for i in range(n2-length+1):
            if freq1 == freq2:
                return True
            if i+length==n2:
                break
            letter = s2[i]
            freq2[letter]-=1
            if freq2[letter]==0:
                del freq2[letter]
            freq2[s2[i+length]]=freq2.get(s2[i+length],0)+1
        return False

