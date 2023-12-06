from random import randint


class GoalsCounter:
    @staticmethod
    def get_count():
        goals_count = randint(0, 5)
        return goals_count
