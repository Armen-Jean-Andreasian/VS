# configuration imports
from champions_league.data.config.filepaths import groups_json_filepath, match_history_txt_filepath

# other packages import
from src.file_manager.JSON.read_file import ReadJsonFile
from src.file_manager.TXT.write_file import WriteTextFile

# local scripts import
from draws import PairDraws
from champions_league.src.generating_score import GoalsCounter
from champions_league.src.refresh_standings import UpdateStandings


class GroupStage:
    def __init__(self, groups_standings_fp: str = None, match_history_fp: str = None):
        self.match_history_fp = match_history_fp if match_history_fp else match_history_txt_filepath
        self.groups_standings_fp = groups_standings_fp if groups_standings_fp else groups_json_filepath

        self.GROUP_STANDINGS: dict[str:dict[str:int]] = None
        self.SCHEDULE: dict[str:list[tuple[str, str]]] = None
        self.match_history = list()

    def get_groups(self) -> dict[str:dict[str:int]]:
        """Reading json file with draws"""
        # {'Group A': {'Inter': 0, 'Barcelona': 0, 'PSV': 0, 'Juventus': 0},}
        self.GROUP_STANDINGS = ReadJsonFile.read(self.groups_standings_fp)
        return self

    def schedule_matches(self) -> dict[str:list[tuple[str, str]]]:
        """
        {'Group A': {'Inter': 0, 'Barcelona': 0, 'PSV': 0, 'Juventus': 0}
        ->
        {'Group A': [('Inter', 'Barcelona'), ('Inter', 'PSV'), ('Inter', 'Juventus'),
                    ('Barcelona', 'PSV'), ('Barcelona', 'Juventus'), ('PSV', 'Juventus')],}
        """
        self.SCHEDULE = {key: PairDraws(list(value.keys())).get_pairs() for key, value in self.GROUP_STANDINGS.items()}
        return self

    @property
    def get_final_standings(self):
        return self.GROUP_STANDINGS

    @property
    def get_history_of_matches(self):
        return self.match_history


class PlayMatches(GroupStage):
    def play_matches(self):
        for group_name, pair_of_teams in self.SCHEDULE.items():
            for team1, team2 in pair_of_teams:

                team1_goals_count: int = GoalsCounter.get_count()
                team2_goals_count: int = GoalsCounter.get_count()

                if team1_goals_count > team2_goals_count:
                    self.add_points(group_name=group_name, team_name=team1, point=3)
                elif team2_goals_count > team1_goals_count:
                    self.add_points(group_name=group_name, team_name=team2, point=3)
                else:
                    self.add_points(group_name=group_name, team_name=team1, point=1)
                    self.add_points(group_name=group_name, team_name=team2, point=1)

                result = f"{team1} vs {team2} {team1_goals_count}:{team2_goals_count}"
                # example of result: 'Real Madrid vs Barcelona 5:0'
                self.match_history.append(result)

    def add_points(self, group_name, team_name, point):
        """Adds 1 or 3 points to each club in their groups """
        self.GROUP_STANDINGS[group_name][team_name] += point
        return self


class SaveResults(PlayMatches):
    def save_results(self):
        str_match_history = str(self.match_history)
        str_group_standings = str(self.GROUP_STANDINGS)

        memo = str_match_history + 2 * '\n' + str_group_standings
        WriteTextFile.write(filepath=self.match_history_fp, content=memo)
        return memo


class PlayMatchesMain(SaveResults):
    def main(self):
        self.get_groups()
        self.schedule_matches()
        self.play_matches()
        self.GROUP_STANDINGS = UpdateStandings.sort_by_points(self.GROUP_STANDINGS)

        return self.save_results()


if __name__ == '__main__':
    json_fp = '../../../' + groups_json_filepath
    txt_fp = '../../../' + match_history_txt_filepath
    matches = PlayMatchesMain(groups_standings_fp=json_fp, match_history_fp=txt_fp)
    f = matches.main()
    print(f)
