class Solution:
    def searchMatrix(self, grid: List[List[int]], target: int) -> bool:
        start = 0
        end = len(grid) * len(grid[0])-1
        while start <= end:
            mid = (start + end)//2
            if grid[mid//len(grid[0])][mid%len(grid[0])] == target:
                return True
            if grid[mid//len(grid[0])][mid%len(grid[0])] > target:
                end = mid-1
            else:
                start = mid +1
        return False