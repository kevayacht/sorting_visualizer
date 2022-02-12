from abc import ABC, abstractmethod


class Framework(ABC):
    @abstractmethod
    def draw(self, data: list, colors: list) -> None:
        pass
