class RemoveCandidate(object):
    def __init__(self, x, y, candidates, strategy, difficulty) -> None:
        self.x = x
        self.y = y
        self.candidates = candidates
        self.strategy = strategy
        self.difficulty = difficulty

    def __repr__(self) -> str:
        return f"({self.x}, {self.y}) {self.candidates} - {self.strategy}"
