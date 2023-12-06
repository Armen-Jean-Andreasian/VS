from football.champions_league.general.config import groups_json_filepath, match_history_txt_filepath
from football.champions_league.group_stage import PlayCLGroupStageMatches

if __name__ == '__main__':
    json_fp = '../' + groups_json_filepath
    txt_fp = '../' + match_history_txt_filepath
    matches = PlayCLGroupStageMatches(groups_standings_fp=json_fp, match_history_fp=txt_fp)
    f = matches.main()
    print(f)


