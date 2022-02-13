import time
import random

from app.algorithms import Algorithm
from app.colors import BLUE, YELLOW
from app.framework.framework import Framework


class RandomSort(Algorithm):
    def __init__(self):
        self.trys = []

    def execute(self, data: list, timeTick: float, framework: Framework) -> None:
        random.shuffle(data)
        framework.draw(data, [[YELLOW] for x in range(len(data))])
        time.sleep(timeTick)

        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                self.trys.append(1)
                self.execute(data, timeTick, framework)

        framework.draw(data, [BLUE for x in range(len(data))])
