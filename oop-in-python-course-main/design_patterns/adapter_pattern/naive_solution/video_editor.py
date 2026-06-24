from design_patterns.adapter_pattern.naive_solution.color import Color


class VideoEditor:
    def __init__(self, video):
        self.video = video

    def apply_color(self, color: Color):
        color.apply(self.video)
