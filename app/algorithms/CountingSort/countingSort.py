import time

from app.algorithms import Algorithm
from app.colors import RED, BLUE
from app.framework.framework import Framework


class CountingSort(Algorithm):
    def execute(self, data: list, timeTick: float, framework: Framework) -> None:
        mval = 0
        for i in range(len(data)):
            framework.draw(data, [RED if x == i else [BLUE] for x in range(len(data))])
            time.sleep(timeTick)
            if data[i] > mval:
                mval = data[i]

        buckets = [0 for i in range(mval + 1)]

        for i in data:
            buckets[i] += 1

        i = 0
        for j in range(mval + 1):
            for _ in range(buckets[j]):
                data[i] = j
                i += 1

        framework.draw(data, [BLUE for x in range(len(data))])
        time.sleep(timeTick)
