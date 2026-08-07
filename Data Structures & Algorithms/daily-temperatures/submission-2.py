class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        solution = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                solution[stack_index] = i - stack_index
            stack.append((t, i))
        return solution
        