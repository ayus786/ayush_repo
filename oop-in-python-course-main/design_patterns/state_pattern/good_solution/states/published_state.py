from design_patterns.state_pattern.good_solution.states.state import State


class PublishedState(State):
    def __init__(self, document):
        self._document = document

    def publish(self):
        pass  # do nothing
