from football.champions_league.general.match_history import MATCH_HISTORY


class MatchHistoryUpdater:
    @staticmethod
    def update_records(result):
        MATCH_HISTORY.append(result)
