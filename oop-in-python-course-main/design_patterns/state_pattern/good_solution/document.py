from design_patterns.state_pattern.good_solution.states.draft_state import (
    DraftState,
)


class Document:
    def __init__(self, current_user_role):
        self.state = DraftState(self)  # New documents have draft state by default
        self.current_user_role = current_user_role

    def publish(self):
        self.state.publish()
