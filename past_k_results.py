from extract_data import FootballData
import extract_data as ed


def average(numbers_list):
    return float(sum(numbers_list)) / len(numbers_list)


class PastKResults:
    def __init__(self, season, K=4):
        self.football_data = FootballData()
        self.season_data = self.football_data.seasons_data[season]
        self.K = K

    def get_past_K_games_results(self, team, game_date):
        k = 0
        K_last_full_time_results = []
        for item in self.season_data:
            if ed.compare_datetime(game_date, item[1]):
                if item[2] == team:
                    k = k + 1
                    if item[6] == 'H':
                        K_last_full_time_results.append(3)
                    elif item[6] == 'A':
                        K_last_full_time_results.append(1)
                    else:
                        K_last_full_time_results.append(2)
                if item[3] == team:
                    k = k + 1
                    if item[6] == 'A':
                        K_last_full_time_results.append(3)
                    elif item[6] == 'H':
                        K_last_full_time_results.append(1)
                    else:
                        K_last_full_time_results.append(2)
                if k >= self.K:
                    return K_last_full_time_results
        return None

    def get_two_teams_past_K_results(self, home_team, away_team, date):

        two_teams_past_K_results = {}
        two_teams_past_K_results[home_team] = self.get_past_K_games_results(home_team, date)
        two_teams_past_K_results[away_team] = self.get_past_K_games_results(away_team, date)

        return two_teams_past_K_results

    def get_two_teams_average_past_K_results(self, home_team, away_team, date):

        two_team_average_past_k_results = self.get_two_teams_past_K_results(home_team, away_team, date)
        two_team_average_past_k_results[home_team] = average(two_team_average_past_k_results[home_team])
        two_team_average_past_k_results[away_team] = average(two_team_average_past_k_results[away_team])

        return two_team_average_past_k_results


# ----------------------------------
# my own tests
season09 = PastKResults('D2009')
pastk = season09.get_past_K_games_results("Bochum", "23/04/10")
pastkboth = season09.get_two_teams_past_K_results("Bochum", "Stuttgart", "23/04/10")
pastkavg = season09.get_two_teams_average_past_K_results("Bochum", "Stuttgart", "23/04/10")

print(pastk)
print(pastkboth)
print(pastkavg)
# ----------------------------
