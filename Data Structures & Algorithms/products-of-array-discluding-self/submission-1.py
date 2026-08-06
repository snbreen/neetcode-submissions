class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        solution = [1] * n
        prefix = suffix = 1
        for i in range(n):
            solution[i] = prefix
            prefix *= nums[i]

        for i in range(n-1, -1, -1):
            solution[i] *= suffix
            suffix *= nums[i]
        
        return solution
        