from champions_league.data.data import MATCH_HISTORY


class MatchHistory:
    @staticmethod
    def update_records(result):
        MATCH_HISTORY.append(result)
