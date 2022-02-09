from abc import ABC, abstractmethod


# algorithm interface
class Algorithm(ABC):
    @abstractmethod
    def execute(self, data, timeTick, framework) -> None:
        pass
