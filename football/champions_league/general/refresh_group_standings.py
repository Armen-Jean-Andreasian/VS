class UpdateStandings:
    """Updates the order of teams based on the amount of points they earned. High -> Low"""

    @staticmethod
    def sort_by_points(standings: dict):
        for group, team_data in standings.items():
            sorted_teams = sorted(team_data.items(), key=lambda x: x[1], reverse=True)
            standings[group] = dict(sorted_teams)

        return standings


if __name__ == '__main__':
    # Example usage
    teams = {
        'Group A': {'Inter': 6, 'Barcelona': 4, 'PSV': 6, 'Juventus': 1},
        'Group B': {'RB Leipzig': 1, 'VfB Stuttgart': 3, 'Manchester City': 6, 'Borussia Dortmund': 7},
    }
    updated_teams = UpdateStandings.sort_by_points(teams)
    print(updated_teams)
