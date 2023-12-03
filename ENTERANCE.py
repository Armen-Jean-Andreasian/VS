from champions_league.src.group_stage.group_stage import PlayMatchesMain
from champions_league.data.config.filepaths import groups_json_filepath, match_history_txt_filepath


if __name__ == '__main__':
    matches = PlayMatchesMain(groups_standings_fp=groups_json_filepath, match_history_fp=match_history_txt_filepath)
    f = matches.main()
    print(f)
