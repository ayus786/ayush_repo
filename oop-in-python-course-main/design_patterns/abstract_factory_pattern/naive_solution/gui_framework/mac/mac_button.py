from design_patterns.abstract_factory_pattern.naive_solution.gui_framework.button import (
    Button,
)


class MacButton(Button):
    def render(self):
        print("Mac: render button")

    def on_click(self):
        print("Mac: button clicked")
