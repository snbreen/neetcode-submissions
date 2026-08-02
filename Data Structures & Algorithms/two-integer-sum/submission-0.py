class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for index, number in enumerate(nums):
            map[number] = index

        for index, number in enumerate(nums):
            difference = target - number
            if difference in map and map[difference] != index:
                return [index, map[difference]]

        return []
        

        