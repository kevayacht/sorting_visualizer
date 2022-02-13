import time

from app.algorithms import Algorithm
from app.colors import BLUE, PURPLE
from app.framework.framework import Framework


class CocktailSort(Algorithm):
    def execute(self, data: list, timeTick: float, framework: Framework) -> None:
        for i in range(len(data) - 1):

            for j in range(len(data) - 1, 0, -1):
                if data[j] < data[j - 1]:
                    data[j], data[j - 1] = data[j - 1], data[j]
                    framework.draw(data, [PURPLE if x == j else [BLUE] for x in range(len(data))])
                    time.sleep(timeTick)

            for k in range(len(data) - 1):
                if data[k] > data[k + 1]:
                    data[k], data[k + 1] = data[k + 1], data[k]
                    framework.draw(data, [PURPLE if x == k else [BLUE] for x in range(len(data))])
                    time.sleep(timeTick)
