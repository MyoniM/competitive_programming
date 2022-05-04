class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = {0: 0, 1: 0, 2: 0}
        for i in range(len(nums)):
            count[nums[i]] += 1
        nums.clear()
        for i in [0, 1, 2]:
            nums += [i]*count[i]