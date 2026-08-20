class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solution = []
        for i, a in enumerate(nums):
            if a > 0:
                break
            
            if i > 0 and a == nums[i-1]:
                continue

            front, back = i + 1, len(nums) - 1

            while front < back:
                threeSum = a + nums[front] + nums[back]

                if threeSum == 0:
                    solution.append([a, nums[front], nums[back]])
                    front += 1
                    back -= 1
                    while nums[front] == nums[front - 1] and front < back: 
                        front += 1
                elif threeSum > 0:
                    back -= 1
                else:
                    front += 1
        
        return solution



        