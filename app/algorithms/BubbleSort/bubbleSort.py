import time

from app.algorithms.algorithm import Algorithm
from app.colors import YELLOW, BLUE


class BubbleSort(Algorithm):

    def execute(self, data, timeTick, framework) -> None:
        size = len(data)

        for i in range(size - 1):
            for j in range(size - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    framework.draw(data, [YELLOW if x == j or x == j + 1 else BLUE for x in range(len(data))])
                    time.sleep(timeTick)

        framework.draw(data, [BLUE for x in range(len(data))])
