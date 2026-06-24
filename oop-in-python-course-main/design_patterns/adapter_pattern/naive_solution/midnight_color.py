from design_patterns.adapter_pattern.naive_solution.color import Color


class MidnightColor(Color):
    def apply(self, video):
        print("Applying midnight-purple color to video")
