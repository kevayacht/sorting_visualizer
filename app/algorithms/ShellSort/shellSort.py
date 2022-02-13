import time

from app.algorithms.algorithm import Algorithm
from app.colors import RED, BLUE
from app.framework.framework import Framework


class ShellSort(Algorithm):
    def execute(self, data: list, timeTick: float, framework: Framework) -> None:
        n = len(data)
        gap = n//2

        while gap > 0:
            for i in range(gap, n):

                temp = data[i]
                j = i
                while j >= gap and data[j - gap] > temp:
                    data[j] = data[j - gap]
                    framework.draw(data, [RED if x == j or x == j - gap else BLUE for x in range(len(data))])
                    time.sleep(timeTick)
                    j -= gap

                data[j] = temp
                framework.draw(data, [RED if x == j or x == temp else BLUE for x in range(len(data))])
                time.sleep(timeTick)
            gap //= 2

