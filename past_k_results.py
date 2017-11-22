from load_data import FootballData
import datetime


def average(numbers_list):
    if numbers_list is not None:
        return float(sum(numbers_list)) / len(numbers_list)
    else:
        return None


class PastKResults:
    def __init__(self, season, K=4):
        self.football_data = FootballData()
        self.season_data = self.football_data.seasons_data[season]
        self.K = K

    def get_past_K_games_results(self, team, game_date):
        k = 0
        K_last_full_time_results = []
        for item in self.season_data:
            if game_date > item[1]:
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

    def get_past_K_avg_results(self, team, game_date):
        past_K_games = self.get_past_K_games_results(team, game_date)
        return average(past_K_games)

# ----------------------------------
# my own tests
# season14 = PastKResults('D2014')
# print(season14.get_past_K_games_results("Bayern-Munich", datetime.date(2015, 2, 14)))
# print(season14.get_past_K_avg_results("Bayern Munich", datetime.date(2015, 2, 14)))
#
# print(pastk)
# print(pastkboth)
# print(pastkavg)
# ----------------------------
