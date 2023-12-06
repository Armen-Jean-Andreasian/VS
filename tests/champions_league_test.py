from football.champions_league.group_stage.make_groups import MakeGroupsMain
from football.data import all_teams


groups = MakeGroupsMain(all_teams)
res = groups.draw()

print(res)
