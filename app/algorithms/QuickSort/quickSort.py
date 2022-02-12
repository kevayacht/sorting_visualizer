import time

from app.algorithms.algorithm import Algorithm
from app.colors import BLUE, YELLOW, LIGHT_GRAY, RED, LIGHT_GREEN, DARK_BLUE
from app.framework.framework import Framework


class QuickSort(Algorithm):

    def execute(self, data: list, timeTick: float, framework: Framework) -> None:
        self.quick_sort(data, 0, len(data) - 1, timeTick, framework)

    def quick_sort(self, data, low, high, timeTick, framework):
        if low < high:
            pi = self.partition(data, low, high, timeTick, framework)

            self.quick_sort(data, low, pi - 1, timeTick, framework)
            self.quick_sort(data, pi + 1, high, timeTick, framework)

        framework.draw(data, [BLUE for x in range(len(data))])

    def partition(self, data, low, high, timeTick, framework) -> int:
        i = low - 1
        pivot = data[high]

        for j in range(low, high):
            if data[j] <= pivot:
                framework.draw(data, self.getColorArray(data, low, high, i, j, True))
                time.sleep(timeTick)
                i += 1
                data[i], data[j] = data[j], data[i]
            framework.draw(data, self.getColorArray(data, low, high, i, j))
            time.sleep(timeTick)

        framework.draw(data, self.getColorArray(data, low, high, i, high, True))
        time.sleep(timeTick)
        data[i + 1], data[high] = data[high], data[i + 1]

        return i + 1

    @staticmethod
    def getColorArray(data, head, tail, border, index, isSwapping=False) -> list:
        colorArray = []
        for i in range(len(data)):
            if head <= i <= tail:
                colorArray.append(LIGHT_GRAY)
            else:
                colorArray.append(BLUE)

            if i == tail:
                colorArray[i] = DARK_BLUE
            elif i == border:
                colorArray[i] = RED
            elif i == index:
                colorArray[i] = YELLOW
            if isSwapping:
                if i == border or i == index:
                    colorArray[i] = LIGHT_GREEN

        return colorArray
