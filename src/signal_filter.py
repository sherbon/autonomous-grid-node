class MovingAverageFilter:
    """Mathematical data smoothing block to eliminate electrical sensor bus noise."""
    def __init__(self, window_size=3):
        self.window_size = window_size
        self.history = []

    def filter_noise(self, new_reading):
        self.history.append(new_reading)
        if len(self.history) > self.window_size:
            self.history.pop(0)
        return sum(self.history) / len(self.history)
