class Solution:
    def merge(self, arr: List[List[int]]) -> List[List[int]]:
            arr.sort()
            i = 1

            while i < len(arr):
                if arr[i-1][1] >= arr[i][0]:
                    if arr[i-1][1] > arr[i][1]:
                        arr.pop(i)
                        continue
                    arr[i-1] = [arr[i-1][0], arr[i][1]]
                    arr.pop(i)
                else:
                    i+=1
            return arr

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        if len(intervals) == 0:
            intervals.append(newInterval)
            return intervals
        intervals.append(newInterval)
        intervals.sort()
        print(intervals)
        return self.merge(intervals)
        