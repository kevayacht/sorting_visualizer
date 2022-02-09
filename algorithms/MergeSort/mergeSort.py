import time

from algorithms.algorithm import Algorithm
from colors import YELLOW, BLUE, PURPLE, DARK_BLUE


class MergeSort(Algorithm):

    def execute(self, data, timeTick, framework) -> None:
        self.recursive_merge_sort(data, 0, len(data) - 1, timeTick, framework)

    def recursive_merge_sort(self, data, start, end, timeTick, framework):
        if start < end:
            mid = int((start + end) / 2)
            self.recursive_merge_sort(data, start, mid, timeTick, framework)
            self.recursive_merge_sort(data, mid + 1, end, timeTick, framework)

            self.merge(data, start, mid, end)

            arrayColorCodes = [
                PURPLE if start <= x < mid else
                YELLOW if x == mid else
                DARK_BLUE if mid < x <= end else
                BLUE for x in range(len(data))
            ]
            framework.drawData(data, arrayColorCodes)
            time.sleep(timeTick)

        plainColorArray = [BLUE for x in range(len(data))]
        framework.drawData(data, plainColorArray)

    @staticmethod
    def merge(data, start, mid, end):
        temp_array = []
        a = start
        b = mid + 1

        for i in range(start, end + 1):
            if a > mid:
                temp_array.append(data[b])
                b += 1
            elif b > end:
                temp_array.append(data[a])
                a += 1
            elif data[a] < data[b]:
                temp_array.append(data[a])
                a += 1
            else:
                temp_array.append(data[b])
                b += 1

        for a in range(len(temp_array)):
            data[start] = temp_array[a]
            start += 1
