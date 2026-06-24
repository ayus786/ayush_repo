# This is an alternative solution to RainbowColor, using inheritance instead of composition

from design_patterns.adapter_pattern.naive_solution.third_party_color_library.rainbow import (
    Rainbow,
)
from design_patterns.adapter_pattern.naive_solution.color import Color
from design_patterns.adapter_pattern.naive_solution.video import Video

class RainbowAdapter(Rainbow, Color):
    def apply(self, video: Video):
        self.setup()
        self.update(video)
