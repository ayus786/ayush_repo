from design_patterns.abstract_factory_pattern.naive_solution.gui_framework.checkbox import (
    Checkbox,
)


class WindowsCheckbox(Checkbox):
    def render(self):
        print("Windows: render checkbox")

    def on_select(self):
        print("Windows: checkbox selected")
