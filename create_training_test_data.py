import past_k_results
import past_k_features
import load_data
import numpy as np
import pandas as pd
import random


def encode_label_to_int(label):
    if label == 'H':
        return 1
    elif label == 'A':
        return -1
    else:
        return 0


def remove_nan(array):
    for line in array:
        if np.isnan(line).any():
            array.remove(line)


class TrainingTestDataGenerator:
    # use years 2004-2015 as training data, years 2016 and 2017 as test data
    def __init__(self):
        self.football_data = load_data.FootballData().seasons_data
        self.train_seasons = {'D2006', 'D2007', 'D2008', 'D2009', 'D2010', 'D2011', 'D2012',
                              'D2013', 'D2014', 'D2015'}
        self.test_seasons = {'D2016', 'D2017'}
        self.train_data = []
        self.test_data = []
        # self.train_data = {season: self.football_data[season] for season in self.train_seasons}
        # self.test_data = {season: self.football_data[season] for season in self.test_seasons}

    def get_feature_data(self, team, game_date, season):

        past_results = past_k_results.PastKResults(season)
        past_features = past_k_features.PastKFeatures(season)

        avg_results = past_results.get_past_K_avg_results(team, game_date)
        avg_shots_on_target = past_features.get_feature_avg_past_K(team, game_date, 12)
        avg_corners = past_features.get_feature_avg_past_K(team, game_date, 16)
        avg_goals = past_features.get_feature_avg_past_K(team, game_date, 4)

        team_feature = [avg_results, avg_goals, avg_shots_on_target, avg_corners]

        return team_feature

    def get_features_of_a_game(self, home_team, away_team, game_date, season):

        feature_dict = {home_team: self.get_feature_data(home_team, game_date, season),
                        away_team: self.get_feature_data(away_team, game_date, season)}

        return (feature_dict)

    def get_label(self, home_team, away_team, game_date, season):
        season_data = self.football_data[season]
        for item in season_data:
            if (game_date == item[1]) and item[2] == home_team and item[3] == away_team:
                return item[6]

    def combine_label_and_features(self, home_team, away_team, game_date, season):
        label = self.get_label(home_team, away_team, game_date, season)

        temp = self.get_features_of_a_game(home_team, away_team, game_date, season)

        temp[home_team].extend(temp[away_team])

        temp[home_team].insert(0, encode_label_to_int(label))

        return temp[home_team]

    def get_features_one_season(self, season):
        all_features = []
        for x in self.football_data[season]:
            line = self.combine_label_and_features(x[2], x[3], x[1], season)
            if not any(elem is None for elem in line):
                all_features.append(line)
        # for better training, shuffle data
        random.shuffle(all_features)
        X = []
        y = []
        for item in all_features:
            X.append(item[1:])
            y.append(item[0])
        return X, y

    def concatenate_training_test_data(self):
        X_train = []
        X_test = []
        y_train = []
        y_test = []
        for season in self.train_seasons:
            X, y = self.get_features_one_season(season)
            X_train.append(X)
            y_train.append(y)
        for season in self.test_seasons:
            X, y = self.get_features_one_season(season)
            X_test.append(X)
            y_test.append(y)
        save_training_test_data(X_train, X_test, y_train, y_test)

        return X_train, X_test, y_train, y_test


def save_training_test_data(X_train, X_test, y_train, y_test):
    df_Xtrain = pd.DataFrame(X_train)
    df_Xtest = pd.DataFrame(X_test)
    df_ytrain = pd.DataFrame(y_train)
    df_ytest = pd.DataFrame(y_test)

    df_Xtrain.to_csv('Xtrain.csv', header=False, index=False)
    df_Xtest.to_csv('Xtest.csv', header=False, index=False)
    df_ytrain.to_csv('ytrain.csv', header=False, index=False)
    df_ytest.to_csv('ytest.csv', header=False, index=False)


# def update_training_data():


# gameP = GamePredictor()
# gameP.doSVMOnline()
feature_extractor = TrainingTestDataGenerator()
# print(feature_extractor.combine_label_and_features('Bayern-Munich', 'Wolfsburg', datetime.date(2014, 8, 22), 'D2014'))
feature_extractor.concatenate_training_test_data()

