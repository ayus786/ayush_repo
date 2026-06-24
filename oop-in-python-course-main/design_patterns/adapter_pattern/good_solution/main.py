# Run with: `python -m design_patterns.adapter_pattern.good_solution.main`

from design_patterns.adapter_pattern.naive_solution.video import Video
from design_patterns.adapter_pattern.naive_solution.video_editor import VideoEditor
from design_patterns.adapter_pattern.naive_solution.black_and_white_color import (
    BlackAndWhiteColor,
)
from design_patterns.adapter_pattern.naive_solution.third_party_color_library.rainbow import (
    Rainbow,
)

# Now we can import our adapter class
from design_patterns.adapter_pattern.good_solution.rainbow_color import RainbowColor
from design_patterns.adapter_pattern.good_solution.rainbow_adapter import RainbowAdapter

video = Video()
video_editor = VideoEditor(video)

# Applying one of our own colors
video_editor.apply_color(BlackAndWhiteColor())
# Logs:
# Applying black and white color to video

# We can now apply the rainbow color to our videos, just like the other colors:
video_editor.apply_color(RainbowColor(Rainbow()))
# Logs:
# Setting up rainbow filter
# Applying rainbow filter to video

video_editor.apply_color(RainbowAdapter())
