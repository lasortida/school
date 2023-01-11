class Road:
    def __init__(self, length, width):
        self.length = length if length > 0 else 0
        self.width = width if width > 0 else 0
