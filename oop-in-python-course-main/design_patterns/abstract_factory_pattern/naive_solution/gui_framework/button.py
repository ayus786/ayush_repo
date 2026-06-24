from abc import abstractmethod
from design_patterns.abstract_factory_pattern.naive_solution.gui_framework.ui_component import (
    UIComponent,
)


class Button(UIComponent):
    """Interface for a button UI component"""

    @abstractmethod
    def on_click(self):
        """Handle the button click event"""
        pass

    # Other methods specific to buttons can be defined here...
