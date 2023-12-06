from football.champions_league import PlayCLGroupStageMatches
from football.champions_league.general.config.filepaths import groups_json_filepath, match_history_txt_filepath


if __name__ == '__main__':
    matches = PlayCLGroupStageMatches(groups_standings_fp=groups_json_filepath, match_history_fp=match_history_txt_filepath)
    f = matches.main()
    print(f)
