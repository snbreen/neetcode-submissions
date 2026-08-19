class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        front = 0
        back = n - 1
        while front < back:
            if numbers[front] + numbers[back] == target:
                return [front + 1, back + 1]
            
            if numbers[front] + numbers[back] < target:
                front += 1
                continue 
            if numbers[front] + numbers[back] > target:
                back -= 1
                continue
        

        