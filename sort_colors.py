class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = {}
        for i in range(len(nums)):
            if nums[i] not in count: count[nums[i]] = 0
            count[nums[i]]+=1
        nums.clear() 
        for i in [0,1,2]:
            if i in count: nums +=  [i]*count[i]
