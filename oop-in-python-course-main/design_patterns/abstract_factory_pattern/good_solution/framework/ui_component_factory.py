from abc import ABC, abstractmethod
from design_patterns.abstract_factory_pattern.naive_solution.gui_framework.button import (
    Button,
)
from design_patterns.abstract_factory_pattern.naive_solution.gui_framework.checkbox import (
    Checkbox,
)


class UIComponentFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass
