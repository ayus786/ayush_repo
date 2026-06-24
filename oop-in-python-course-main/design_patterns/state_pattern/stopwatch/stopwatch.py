# Run with `python -m design_patterns.state_pattern.stopwatch.stopwatch`


class Stopwatch:
    def __init__(self):
        self._is_running = False  # Initialize as not running

    def click(self):
        if self._is_running:
            self._is_running = False
            print("Stopped")
        else:
            self._is_running = True
            print("Running")


stopwatch = Stopwatch()
stopwatch.click()  # Output: Running
stopwatch.click()  # Output: Stopped
stopwatch.click()  # Output: Running
