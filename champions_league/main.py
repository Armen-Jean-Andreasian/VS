from draws import PairDraws
from champions_league.data.data import MATCH_HISTORY, TEAMS_TIER_ONE_16
from scripts import GoalsCounter, MatchHistory, UpdateStandings


class ChampionsLeagueGroupStage:
    def __init__(self):
        teams_list = list(TEAMS_TIER_ONE_16.keys())
        self.schedule = PairDraws(teams_list).get_pairs()

    def play_matches(self):
        for team1, team2 in self.schedule:
            team1_goals_count = GoalsCounter.get_count()
            team2_goals_count = GoalsCounter.get_count()

            if team1_goals_count > team2_goals_count:
                TEAMS_TIER_ONE_16[team1] += 3
            elif team2_goals_count > team1_goals_count:
                TEAMS_TIER_ONE_16[team2] += 3
            else:
                TEAMS_TIER_ONE_16[team1] += 1
                TEAMS_TIER_ONE_16[team2] += 1

            # example of result: 'Real Madrid vs Barcelona 5:0'
            result = f"{team1} vs {team2} {team1_goals_count}:{team2_goals_count}"
            MatchHistory.update_records(result)


class ChampionsLeagueFinal:
    def __init__(self):
        self.games = None
        self.result = []
        self.winner = None

    def sort_by_points(self):
        sorted_teams = UpdateStandings.sort_by_points()
        final_game: tuple = sorted_teams[0][0], sorted_teams[1][0]
        third_place_game: tuple = sorted_teams[2][0], sorted_teams[3][0]

        self.games = [third_place_game, final_game]
        return self

    def play_matches(self):
        self.sort_by_points()
        for team1, team2 in self.games:
            team1_goals_count = GoalsCounter.get_count()
            team2_goals_count = GoalsCounter.get_count()

            result = f"{team1} vs {team2} {team1_goals_count}:{team2_goals_count}"
            MatchHistory.update_records(result)
        return self.result


class ChampionsLeague:
    def __init__(self):
        self.group_stage = ChampionsLeagueGroupStage()
        self.final = ChampionsLeagueFinal()

        self.match_history = None
        self.team_points = None

    def play_competition(self):
        self.group_stage.play_matches()
        self.final.play_matches()
        self.__update_records()
        return None

    def __update_records(self):
        self.match_history = MATCH_HISTORY
        self.team_points = TEAMS_TIER_ONE_16
        return self

    @property
    def get_match_history(self):
        return self.match_history

    @property
    def get_team_standings(self):
        return self.team_points

    def __repr__(self):
        example = """
Example of usage:        

champs = ChampionsLeague()
champs.play_competition()
print(champs.get_team_standings)
print(champs.get_match_history)
"""
        return example



champs = ChampionsLeague()
print(champs)

champs.play_competition()
print(champs.get_team_standings)
print(champs.get_match_history)


