from design_patterns.abstract_factory_pattern.naive_solution.gui_framework.mac.mac_button import (
    MacButton,
)
from design_patterns.abstract_factory_pattern.naive_solution.gui_framework.mac.mac_checkbox import (
    MacCheckbox,
)
from design_patterns.abstract_factory_pattern.good_solution.framework.ui_component_factory import (
    UIComponentFactory,
)
from design_patterns.abstract_factory_pattern.naive_solution.gui_framework.button import (
    Button,
)
from design_patterns.abstract_factory_pattern.naive_solution.gui_framework.checkbox import (
    Checkbox,
)


class MacUIComponentFactory(UIComponentFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()
