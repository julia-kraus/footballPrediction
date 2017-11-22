import load_data as ed
import datetime

corners_feature = 16
target_shots_feature = 12
goals_feature = 4


class PastKFeatures:
    def __init__(self, season, K=4):
        self.football_data = ed.FootballData().seasons_data[season]
        self.performance = []
        self.K = K

    def get_feature_past_K(self, team, game_date, feature):
        k = 0
        full_time_result = []  # full time result
        for item in self.football_data:
            if game_date > item[1]:
                if item[2] == team:
                    k += 1
                    full_time_result.append(int(item[feature]))
                if item[3] == team:
                    k = k + 1
                    full_time_result.append(int(item[feature + 1]))
                if k >= self.K:
                    return full_time_result
        return None

    def get_feature_avg_past_K(self, team, game_date, feature):

        one_team_past_k_feature_average = self.get_feature_past_K(team, game_date, feature)
        return average(one_team_past_k_feature_average)


def average(numbers_list):
    if numbers_list is not None:
        return float(sum(numbers_list)) / len(numbers_list)
    else:
        return None

# -------------------------------
# my tests
# season14 = PastKFeatures('D2014')
# print(season14.get_feature_past_K('Leverkusen', datetime.date(2015, 2, 21), corners_feature))
# print(season14.get_feature_avg_past_K('Bayern-Munich', datetime.date(2015, 2, 21), corners_feature))

# season09 = PastKFeatures('D2009')
# print(season09.get_feature_past_K('Mainz', '27/03/10', goals_feature))
# print(season09.get_feature_avg_past_K('Wolfsburg', '27/03/10', goals_feature))



# --------------------------------
