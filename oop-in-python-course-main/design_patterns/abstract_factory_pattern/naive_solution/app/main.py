# Run with: `python -m design_patterns.abstract_factory_pattern.naive_solution.app.main`

from design_patterns.abstract_factory_pattern.naive_solution.gui_framework.operating_system_type import (
    OperatingSystemType,
)
from design_patterns.abstract_factory_pattern.naive_solution.app.user_settings_form import (
    UserSettingsForm,
)

os = OperatingSystemType.MAC  # Set the operating system type

user_settings_form = UserSettingsForm()
user_settings_form.render(os)

# Logs:
# Mac: render button
# Mac: render checkbox
