class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash_map = {}
        count = 0
        for i,e in enumerate(nums):
            if e  in hash_map:
                count+=hash_map[e]
                hash_map[e] += 1
            else:
                hash_map[e] = 1
        
        return count
