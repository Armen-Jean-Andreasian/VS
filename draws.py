class PairDraws:
    def __init__(self, list_of_teams):
        self.__pairs = []
        self.__list_of_teams = list_of_teams
        # self.list_of_teams = list(TEAMS.keys())

    def __make_pairs(self):
        current_index = 0
        end_index = len(self.__list_of_teams)

        while current_index != end_index:
            team1 = self.__list_of_teams[current_index]

            for team2 in self.__list_of_teams[current_index + 1:]:
                self.__pairs.append((team1, team2))
            current_index += 1
        return self

    def get_pairs(self):
        self.__make_pairs()
        return self.__pairs
