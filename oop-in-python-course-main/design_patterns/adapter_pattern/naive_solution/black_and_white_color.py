from design_patterns.adapter_pattern.naive_solution.color import Color


class BlackAndWhiteColor(Color):
    def apply(self, video):
        print("Applying black and white color to video")
