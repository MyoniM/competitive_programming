class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        result = []
        stop = False
        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)
                stop = True
            elif(stop):
                break
        return result
