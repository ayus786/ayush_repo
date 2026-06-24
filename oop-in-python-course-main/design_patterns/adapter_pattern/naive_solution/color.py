from abc import ABC, abstractmethod

class Color(ABC):
    @abstractmethod
    def apply(self, video):
        pass
