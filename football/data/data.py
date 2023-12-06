class DataBase:
    TEAMS_TIER_ONE_16 = {
        'Real Madrid': 0, 'Barcelona': 0, 'Milan': 0, 'Inter': 0, 'Juventus': 0,
        'Chelsea': 0, 'Arsenal': 0, 'Liverpool': 0, 'Manchester City': 0, 'Manchester United': 0,
        'Bayern Munich': 0, 'Borussia Dortmund': 0, 'PSG': 0, 'Ajax': 0, 'PSV': 0,
        'Tottenham': 0,
    }
    TEAMS_TIER_TWO_16 = {
        'Valencia': 0, 'Sevilla': 0, 'Villarreal': 0,
        'Everton': 0, 'Newcastle ': 0, 'Leicester City': 0,
        'Bayer Leverkusen': 0, 'VfB Stuttgart': 0, 'RB Leipzig': 0,
        'Roma': 0, 'Lazio': 0, 'Napoli': 0,
        'Porto': 0, 'Benfica': 0,
        'Lion': 0, 'Marseille': 0,
    }

    ALL_TEAMS = {}
    ALL_TEAMS.update(TEAMS_TIER_ONE_16)
    ALL_TEAMS.update(TEAMS_TIER_TWO_16)


    def initialize(self) -> tuple[list[str], list[str], list[str]]:
        return (list(self.TEAMS_TIER_ONE_16.keys()),
                list(self.TEAMS_TIER_TWO_16.keys()),
                list(self.ALL_TEAMS.keys()))


tier_one_teams, tier_two_teams, all_teams = DataBase().initialize()
