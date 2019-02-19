import pandas
from game import Player, Team
import logging

logger = logging.getLogger()

def create_teams(team_details, roster):
    team_one = Team(team_details['Unnamed: 1'][0], team_details['Unnamed: 1'][1])

    logger.info('Creating team %s %s' % (team_one.league, team_one.name))

    for i, number in enumerate(roster[' Skater #']):
        try:
            num = int(number)
            name = roster[' Skater Name'][i]
            logger.info('Found player number %d: %s' % (num, name))
            team_one.add_player(Player(name, num))
        except:
            break

    team_two = Team(team_details['Unnamed: 8'][0], team_details['Unnamed: 8'][1])

    logger.info('Creating team %s %s' % (team_two.league, team_two.name))

    for i, number in enumerate(roster[' Skater #.1']):
        try:
            num = int(number)
            name = roster[' Skater Name.1'][i]
            logger.info('Found player number %d: %s' % (num, name))
            team_two.add_player(Player(name, num))
        except:
            break

    return team_one, team_two

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    roster = pandas.read_excel('STATS-2018-07-21_LRGC_vs_BATH.xlsx', sheet_name='IGRF', skiprows=12)
    team_details = pandas.read_excel('STATS-2018-07-21_LRGC_vs_BATH.xlsx', sheet_name='IGRF', skiprows=8)

    team_one, team_two = create_teams(team_details, roster)