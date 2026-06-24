# Run file with: `python -m  design_patterns.adapter_pattern.naive_solution.main`

from design_patterns.adapter_pattern.naive_solution.video import Video
from design_patterns.adapter_pattern.naive_solution.video_editor import VideoEditor
from design_patterns.adapter_pattern.naive_solution.black_and_white_color import (
    BlackAndWhiteColor,
)
from design_patterns.adapter_pattern.naive_solution.third_party_color_library.rainbow import (
    Rainbow,
)

video = Video()
video_editor = VideoEditor(video)

video_editor.apply_color(BlackAndWhiteColor())
# Output: Applying black and white color to video

# Applying a third-party lib color: ERROR: Argument of type "Rainbow" cannot be assigned to parameter "color" of type "Color" in function "apply_color"
# video_editor.apply_color(Rainbow())
