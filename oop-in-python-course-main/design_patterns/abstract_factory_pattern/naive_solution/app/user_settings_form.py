from design_patterns.abstract_factory_pattern.naive_solution.gui_framework.operating_system_type import (
    OperatingSystemType,
)

from design_patterns.abstract_factory_pattern.naive_solution.gui_framework.windows.windows_button import (
    WindowsButton,
)
from design_patterns.abstract_factory_pattern.naive_solution.gui_framework.windows.windows_checkbox import (
    WindowsCheckbox,
)
from design_patterns.abstract_factory_pattern.naive_solution.gui_framework.mac.mac_button import (
    MacButton,
)
from design_patterns.abstract_factory_pattern.naive_solution.gui_framework.mac.mac_checkbox import (
    MacCheckbox,
)


class UserSettingsForm:
    def render(self, os: OperatingSystemType):
        # PROBLEM: open-closed principle violated: if add new OS, we have to modify this class
        if os == OperatingSystemType.WINDOWS:
            # PROBLEM: too easy to make mistake -- e.g., easy to accidentally render a Mac button here.
            WindowsButton().render()
            # PROBLEM: UserSettingsForm is tightly coupled to many concrete implementations of widgets.
            WindowsCheckbox().render()
        elif os == OperatingSystemType.MAC:
            MacButton().render()
            MacCheckbox().render()
