class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        front, back = 0, len(height) - 1
        left_max, right_max = height[front], height[back]
        sol = 0
        while front < back:
            if left_max < right_max:
                front += 1
                left_max = max(left_max, height[front])
                sol += left_max - height[front]
            else:
                back -= 1
                right_max = max(right_max, height[back])
                sol += right_max - height[back]
        return sol


        