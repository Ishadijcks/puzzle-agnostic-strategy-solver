class NumberPlaced(object):
    def __init__(self, index, value, strategy, difficulty) -> None:
        self.index = index
        self.value = value
        self.strategy = strategy
        self.difficulty = difficulty

    def __repr__(self) -> str:
        return f"index {self.index}, {self.value} with {self.strategy} ({self.difficulty})"
