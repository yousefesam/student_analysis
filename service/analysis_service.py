class AnalysisService:
    def __init__(self, strategy):
        self.strategy = strategy

    def run(self, students):
        return self.strategy.analyze(students)