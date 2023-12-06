from football.champions_league.general.refresh_group_standings import UpdateStandings
from football.champions_league.group_stage.group_stage import SaveResults


class PlayCLGroupStageMatches(SaveResults):
    def main(self):
        self.get_groups()
        self.schedule_matches()
        self.play_matches()
        self.GROUP_STANDINGS = UpdateStandings.sort_by_points(self.GROUP_STANDINGS)

        return self.save_results()
