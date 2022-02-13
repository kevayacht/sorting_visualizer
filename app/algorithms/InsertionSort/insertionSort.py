import time

from app.algorithms.algorithm import Algorithm
from app.colors import BLUE, YELLOW, PURPLE, RED


class InsertionSort(Algorithm):

    def execute(self, data, timeTick, framework) -> None:

        for i in range(1, len(data)):
            key = data[i]

            j = i - 1
            while j >= 0 and key < data[j]:
                data[j + 1] = data[j]
                j -= 1
                framework.draw(data, [PURPLE if x == i else YELLOW if x == j or x == j + 1 else BLUE for x in range(len(data))])
                time.sleep(timeTick)
            data[j + 1] = key
            framework.draw(data, [RED if x == j + 1 else BLUE for x in range(len(data))])
            time.sleep(timeTick)

        framework.draw(data, [BLUE for x in range(len(data))])
        time.sleep(timeTick)
