from abc import ABC, abstractmethod

from app.framework.framework import Framework


# interface
class Algorithm(ABC):
    @abstractmethod
    def execute(self, data: list, timeTick: float, framework: Framework) -> None:
        pass
