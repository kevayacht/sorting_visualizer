import time

from app.algorithms import Algorithm
from app.colors import RED, BLACK, BLUE
from app.framework.framework import Framework


class OptiBubbleSort(Algorithm):

    def execute(self, data: list, timeTick: float, framework: Framework) -> None:
        n = len(data)
        update = True
        j = 0
        while update and n > 1:
            update = False
            for i in range(len(data) - j - 1):
                if data[i] > data[i + 1]:
                    data[i], data[i + 1] = data[i + 1], data[i]
                    framework.draw(data, [RED if x == i or x == i + 1 else [BLUE] for x in range(len(data))])
                    time.sleep(timeTick)
                    update = True
                else:
                    i += 1
            n -= 1
            j += 1
        framework.draw(data, [BLUE for x in range(len(data))])
