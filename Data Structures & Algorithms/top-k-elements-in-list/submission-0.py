from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        freq_list = []
        for key,value in freq.items():
            freq_list.append([key,value])
        freq_list = sorted(freq_list, key=lambda key: key[1])
        freq_list = freq_list[-k::]
        res=[]
        for i in freq_list:
            res.append(i[0])
        return res

        
