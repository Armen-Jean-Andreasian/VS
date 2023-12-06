from random import choice
from football.champions_league.general.config.filepaths import groups_json_filepath
from shared_scripts.file_manager.JSON.write_file import WriteJsonFile


class MakeGroups:
    """Group consists of 4 teams """

    def __init__(self, teams: list):
        self.list_of_teams = teams

        self.current_group_number = 1
        self.temp_group = list()

        self.results = dict()
        # {"Group A": {"Juventus": 0, "Villarreal": 0, "Manchester City": 0, "Manchester United": 0},}

    def __pick_a_team(self):
        """Picks a random team from the list of teams """
        chosen_team = choice(self.list_of_teams)
        return chosen_team

    def __register_the_team(self, team):
        """Removes the team from the list of teams, adds it to the temp group"""
        self.list_of_teams.remove(team)
        self.temp_group.append(team)
        return self

    def __pack_results(self):
        """Registers the temp results"""
        group_name = self.__name_the_group(self.current_group_number)

        result = {i: 0 for i in self.temp_group}
        """
        Changing the format of self.temp_group
            making it dict
            adding zero next to team name (all clubs have 0 starting points)
            
        Before:
            ['Juventus', 'Villarreal', 'Manchester City', 'Manchester United']
            
        After:
            {'Juventus': 0, 'Villarreal': 0, 'Manchester City': 0, 'Manchester United': 0}
            
        """
        self.results[group_name] = result
        self.__reset_values()

    def __reset_values(self):
        # resetting/updating the values
        self.temp_group = []
        self.current_group_number += 1
        return self

    @classmethod
    def __name_the_group(cls, number: int) -> str:
        """Returns A, B or C depending on the given number"""
        alphabet = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L',
                    13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W',
                    24: 'X', 25: 'Y', 26: 'Z'}

        group_letter = alphabet[number]
        group_name = f"Group {group_letter}"
        return group_name

    def make_groups(self):
        # problem is here
        while self.list_of_teams:
            if len(self.temp_group) < 4:
                # picking a random team from the list, removing it from it, appending to the temp group
                chosen_team = self.__pick_a_team()
                self.__register_the_team(chosen_team)

            elif len(self.temp_group) == 4:
                self.__pack_results()
                # proceeding with current
                chosen_team = self.__pick_a_team()
                self.__register_the_team(chosen_team)

        # if no teams left in self.list_of_teams
        if self.temp_group:
            self.__pack_results()

        return self

    @property
    def get_results(self):
        return self.results


class MakeGroupsMain(MakeGroups):
    def draw(self) -> dict[str:list[str]]:
        self.make_groups()
        return self.get_results

    def save_results(self) -> None:
        return WriteJsonFile.write(filepath=groups_json_filepath, content=self.get_results)



if __name__ == '__main__':
    from football.data.data import all_teams
    grouper = MakeGroupsMain(teams=all_teams)
    results = grouper.draw()
    grouper.save_results()

    print(results)
