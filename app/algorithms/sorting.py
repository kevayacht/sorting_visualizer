from app.algorithms.algorithm import Algorithm
from app.framework.framework import Framework


# factory
class SortingAlgorithm:
    algorithm: Algorithm

    def __init__(self, algorithm: Algorithm = None) -> None:
        if algorithm is not None:
            self.algorithm = algorithm

    def sort(self, data: list, timeTick: float, framework: Framework) -> None:
        self.algorithm.execute(data, timeTick, framework)
