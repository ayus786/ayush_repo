from abc import ABC, abstractmethod

class UIComponent(ABC):
    @abstractmethod
    def render(self):
        """Render the UI component"""
        pass
