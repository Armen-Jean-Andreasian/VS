from game_sim.g import construct_table, games

from draws import PairDraws
from champions_league.src import UpdateStandings

construct_table()

list_of_games = list(games.keys())

drawer = PairDraws(list_of_games)
pairs = drawer.get_pairs()

for game_1, game_2 in pairs:
    choice = input(f'{game_1, game_2} 1 or 2')
    if choice == '1':
        games[game_1] += 3
    elif choice == '2':
        games[game_2] += 3

results = UpdateStandings.sort_by_points(teams=games)
print(results)



