from design_patterns.abstract_factory_pattern.naive_solution.gui_framework.button import (
    Button,
)


class WindowsButton(Button):
    def render(self):
        print("Windows: render button")

    def on_click(self):
        print("Windows: button clicked")
