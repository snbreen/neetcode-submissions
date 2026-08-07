class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        solution = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                stack_index = stack.pop()
                solution[stack_index] = i - stack_index
            stack.append(i)
        return solution
        