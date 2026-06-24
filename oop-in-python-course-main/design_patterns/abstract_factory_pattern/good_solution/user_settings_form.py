from design_patterns.abstract_factory_pattern.good_solution.framework.ui_component_factory import (
    UIComponentFactory,
)


class UserSettingsForm:
    # Polymorphism used here, so this client requires no knowledge of specific uiComponentFactory.
    def render(self, ui_component_factory: UIComponentFactory):
        ui_component_factory.create_button().render()
        ui_component_factory.create_checkbox().render()
