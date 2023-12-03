class GoalsCounter:
    @staticmethod
    def get_count():
        from random import randint
        goals_count = randint(0, 5)
        return goals_count
