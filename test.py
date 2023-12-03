from champions_league import MakeGroupsMain

if __name__ == '__main__':
    def concat_dict(d1, d2):
        main_dict = dict()
        main_dict.update(d1)
        main_dict.update(d2)
        return main_dict

    def get_keys(d):
        return list(d.keys())

    from champions_league.data.data import TEAMS_TIER_ONE_16, TEAMS_TIER_TWO_16

    teams = concat_dict(TEAMS_TIER_ONE_16, TEAMS_TIER_TWO_16)
    teams_list = get_keys(teams)

    grouper = MakeGroupsMain(teams=teams_list)
    results = grouper.draw()
    grouper.save_results()

    print(results)
