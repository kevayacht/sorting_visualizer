import time

from app.algorithms.algorithm import Algorithm
from app.colors import YELLOW, BLUE, PURPLE
from app.framework.framework import Framework


class SelectionSort(Algorithm):
    def execute(self, data: list, timeTick: float, framework: Framework) -> None:
        for i in range(0, len(data) - 1):
            for j in range(i + 1, len(data)):
                if data[i] > data[j]:
                    data[i], data[j] = data[j], data[i]

                    framework.draw(data, [YELLOW if x == j or x == i else BLUE for x in range(len(data))])
                    time.sleep(timeTick)
        framework.draw(data, [BLUE for x in range(len(data))])
