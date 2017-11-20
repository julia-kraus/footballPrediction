import extract_data

K = 4

class PastKFeatures:
    def __init__(self, season):
        self.fbData = FootballData().seasons_data[season]
        self.performance = []
        corners_feature = 16
        target_shots_feature = 12
        goals_feature = 4

    def get_past_K_one_team_one_feature(self, team, game_date, feature):
        # aggregates score of last game concerning certain features. For home team and away team
        # possible features for example corners, target shots, goals
        k = 0
        full_time_result = []  # full time result
        for item in self.fbData:
            if ed.compare_datetime(game_date, item[1]):  # compare the date if it was previous game
                if item[2] == team:
                    k += 1
                    full_time_result.append(int(item[feature]))
                if item[3] == team:
                    k = k + 1
                    full_time_result.append(int(item[feature + 1]))
                if k >= K:
                    return full_time_result
        return None

    def get_past_K_both_teams_one_feature(self, home_team, away_team, game_date, feature):

        past_K_both_teams_one_feature = {home_team: self.get_past_K_one_team_one_feature(home_team, game_date, feature),
                                         away_team: self.get_past_K_one_team_one_feature(away_team, game_date, feature)}

        return past_K_both_teams_one_feature

    def get_average_two_teams_one_feature(self, home_team, away_team, game_date, feature):

        two_team_past_k_feature_average = self.get_past_K_both_teams_one_feature(home_team, away_team, game_date,
                                                                                 feature)
        two_team_past_k_feature_average[home_team] = average(two_team_past_k_feature_average[home_team])
        two_team_past_k_feature_average[away_team] = average(two_team_past_k_feature_average[home_team])

        return two_team_past_k_feature_average


K = 4


def average(list):
    return float(sum(list)) / len(list)

