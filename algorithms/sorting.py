from algorithms.algorithm import Algorithm


class SortingAlgorithm:
    algorithm: Algorithm

    def __init__(self, algorithm: Algorithm = None) -> None:
        if algorithm is not None:
            self.algorithm = algorithm

    def sort(self, data, timeTick, framework) -> None:
        self.algorithm.execute(data, timeTick, framework)
