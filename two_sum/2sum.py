class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #declare the empty dictionary
        map = {}

        #loop through our list to find the two numbers that add to the target

        for key, value in enumerate(nums):
            if target - value in map:
                return [key, map[target -value]]
            map[value] = key