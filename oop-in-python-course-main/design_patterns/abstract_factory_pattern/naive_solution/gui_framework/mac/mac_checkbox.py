from design_patterns.abstract_factory_pattern.naive_solution.gui_framework.checkbox import (
    Checkbox,
)


class MacCheckbox(Checkbox):
    def render(self):
        print("Mac: render checkbox")

    def on_select(self):
        print("Mac: checkbox selected")
