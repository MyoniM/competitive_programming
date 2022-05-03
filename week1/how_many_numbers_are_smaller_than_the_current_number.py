class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        copy_arr = nums[:]

        copy_arr.sort()

        counter_dict = {}
        for i in range(len(copy_arr)):
            if copy_arr[i] not in counter_dict:
                counter_dict[copy_arr[i]] = i

        for i in range(len(nums)):
            nums[i] = counter_dict[nums[i]]

        return nums
