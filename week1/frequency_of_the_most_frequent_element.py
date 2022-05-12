class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
            nums.sort()
            l = r = total = window = 0
            while r < len(nums):
                total += nums[r]
                while(nums[r]*(r-l+1)>total+k):
                    total -= nums[l]
                    l+=1
                window = max(r-l+1,window)
                r += 1
            return window
