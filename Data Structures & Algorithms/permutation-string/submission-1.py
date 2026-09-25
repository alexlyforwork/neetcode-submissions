from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        freq = {}
        n1 = len(s1)
        n2 = len(s2)
        for s in s1:
            freq[s] = freq.get(s,0)+1
        check = {}
        for s in s2[:n1]:
            check[s] = check.get(s,0)+1
        i = 0
        length = n1
        while i+length<=n2:
            if check == freq:
                return True
            check[s2[i]]-=1
            if check[s2[i]]==0:
                del check[s2[i]]
            if i+length==n2:
                break
            check[s2[i+length]]=check.get(s2[i+length],0)+1
            i+=1
        return False

