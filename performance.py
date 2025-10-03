from abc import ABC, abstractmethod

class Performance(ABC):
    def __init__(self, subjects, scores):
        self.__subjects = subjects
        self.__scores = scores

    @property
    def subjects(self):
        return self.__subjects

    @property
    def scores(self):
        return self.__scores

    @abstractmethod
    def average_score(self):
        pass

class RealPerformance(Performance):
    def average_score(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

class DesiredPerformance(Performance):
    def __init__(self, subjects, desired_scores, desired_average):
        super().__init__(subjects, desired_scores)
        self.__desired_average = desired_average

    @property
    def desired_average(self):
        return self.__desired_average

    def average_score(self):
        return self.__desired_average