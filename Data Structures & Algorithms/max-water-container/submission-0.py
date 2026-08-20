class Solution:
    def maxArea(self, heights: List[int]) -> int:
        front, back = 0, len(heights) - 1
        solution = 0
        while front < back:
            area = min(heights[front], heights[back]) * (back - front)
            solution = max(solution, area)
            if heights[front] <= heights[back]:
                front += 1
            else:
                back -= 1
        return solution


        