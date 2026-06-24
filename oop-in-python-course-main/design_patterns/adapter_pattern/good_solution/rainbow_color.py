from design_patterns.adapter_pattern.naive_solution.color import Color
from design_patterns.adapter_pattern.naive_solution.third_party_color_library.rainbow import (
    Rainbow,
)
from design_patterns.adapter_pattern.naive_solution.video import Video

# Adapter class. Rainbow is the adaptee
class RainbowColor(Color):
    def __init__(self, rainbow: Rainbow):
        # "composition" -- RainbowColor is composed of Rainbow. Protected, as clients should only be concerned with applying the rainbow color, not how it is applied (the implementation details).
        self._rainbow = rainbow

    def apply(self, video: Video):
        self._rainbow.setup()
        self._rainbow.update(video)
