import past_k_results
import past_k_features
import past_k_history
import extract_data
import sklearn.svm as svm
from sklearn import preprocessing
import numpy as np


class GamePredictor:
    def __init__(self):
        self.dataSet = extract_data.FootballData().seasons_data
        self.trainSet = []
        self.testSet = []
        self.trainFeatures = []
        self.testFeatures = []
        self.past_k_result = past_k_results
        self.past_k_game_results = past_k_results.PastKResults('D2014')
        self.past_k_game_results15 = past_k_results.PastKResults('D2015')
        self.past_k_game_history = past_k_history.PastKHistory()
        self.past_k_game_perform = past_k_features.PastKFeatures('D2014')
        self.past_k_game_perform15 = past_k_features.PastKFeatures('D2015')

    def get_features_of_a_game(self, home_team, away_team, game_date):

        feature_dict = {home_team: [], away_team: []}

        home_team_feature = []
        away_team_feature = []

        game_results = self.past_k_game_results.get_two_teams_past_K_results(home_team, away_team, game_date)

        game_results[home_team].extend(game_results[away_team])


        game_history = self.past_k_game_history.findAvgHistoryPastKBetweenTwoTeams(home_team, away_team, game_date, 2)

        game_perform_shots = self.past_k_game_perform.get_average_two_teams_one_feature(home_team, away_team, game_date, 11)

        game_perform_shots_on = self.past_k_game_perform.get_average_two_teams_one_feature(home_team, away_team, game_date, 13)

        game_perform_fouls = self.past_k_game_perform.get_average_two_teams_one_feature(home_team, away_team, game_date, 15)

        game_perform_corners = self.past_k_game_perform.get_average_two_teams_one_feature(home_team, away_team, game_date, 17)

        '''add home_team feature data'''
        # home_team_feature.append(game_results)
        # home_team_feature.append(game_results[home_team])
        home_team_feature.append(game_history[home_team])
        home_team_feature.append(game_perform_shots[home_team])
        home_team_feature.append(game_perform_shots_on[home_team])
        home_team_feature.append(game_perform_fouls[home_team])
        home_team_feature.append(game_perform_corners[home_team])

        '''add away_team feature data'''
        # away_team_feature.append(game_results[away_team])
        # away_team_feature.append(game_results[away_team])
        away_team_feature.append(game_history[away_team])
        away_team_feature.append(game_perform_shots[away_team])
        away_team_feature.append(game_perform_shots_on[away_team])
        away_team_feature.append(game_perform_fouls[away_team])
        away_team_feature.append(game_perform_corners[away_team])

        feature_dict[home_team] = home_team_feature
        feature_dict[away_team] = away_team_feature

        return feature_dict

    def transformLabel(self, label):

        if (label == 'H'):
            return 1
        elif (label == 'A'):
            return -1
        else:
            return 0

    def getFeaturesOfSingleGame(self, home_team, away_team, game_date, y, season):

        temp, pr = self.get_features_of_a_game(home_team, away_team, game_date, season)

        temp[home_team].extend(temp[away_team])

        temp[home_team].insert(0, pr)
        temp[home_team].insert(0, self.transformLabel(y))

        return temp[home_team]

    def getFeatureOfSeason(self):

        self.trainFeatures = [self.getFeaturesOfSingleGame(x[2], x[3], x[1], x[6], 'E2014') for x in self.trainSet]
        self.testFeatures = [self.getFeaturesOfSingleGame(x[2], x[3], x[1], x[6], 'E2015') for x in self.testSet]

        x = [x[1:] for x in self.trainFeatures]
        y = [x[0] for x in self.trainFeatures]

        return x, y

    def doSVM(self):

        x, y = self.getFeatureOfSeason()
        print(len(self.trainFeatures))
        # scale_features = preprocessing.scale(np.array(self.trainFeatures,dtype = float))
        detailResults = []
        scale_features = preprocessing.scale(np.array(x, dtype=float))
        print(scale_features)
        tx = [x[1:] for x in self.testFeatures]
        ty = [x[0] for x in self.testFeatures]

        predicthome = [0, 0, 0]
        predictdraw = [0, 0, 0]
        predictaway = [0, 0, 0]

        clf = svm.SVC(kernel='linear')
        clf.decision_function_shape = 'ovr'
        clf.fit(x, y)

        right = 0
        for temp in enumerate(tx):
            detailResult = [self.testSet[temp[0]][2], self.testSet[temp[0]][3], self.testSet[temp[0]][6]]
            if (ty[temp[0]] == 1):
                if (clf.predict(temp[1])[0] == 1):
                    detailResult.append('H')
                    right += 1
                    predicthome[0] += 1
                elif (clf.predict(temp[1])[0] == 0):
                    detailResult.append('D')
                    predicthome[1] += 1
                else:
                    detailResult.append('A')
                    predicthome[2] += 1
            elif (ty[temp[0]] == 0):
                if (clf.predict(temp[1])[0] == 1):
                    detailResult.append('H')
                    predictdraw[0] += 1
                elif (clf.predict(temp[1])[0] == 0):
                    detailResult.append('D')
                    right += 1
                    predictdraw[1] += 1
                else:
                    detailResult.append('A')
                    predictdraw[2] += 1
            else:
                if (clf.predict(temp[1])[0] == 1):
                    detailResult.append('H')
                    predictaway[0] += 1
                elif (clf.predict(temp[1])[0] == 0):
                    detailResult.append('D')
                    predictaway[1] += 1
                else:
                    detailResult.append('A')
                    right += 1
                    predictaway[2] += 1
            detailResults.append(detailResult)

        print(float(right) / len(tx))
        print(detailResults)
        print(predicthome, predictdraw, predictaway)

    def doSVMOnline(self):

        x, y = self.getFeatureOfSeason()
        print(len(self.trainFeatures))
        # scale_features = preprocessing.scale(np.array(self.trainFeatures,dtype = float))
        detailResults = []
        # scale_features = preprocessing.scale(np.array(x,dtype = float))
        # print scale_features
        print(x[-1])
        tx = [x[1:] for x in self.testFeatures]
        ty = [x[0] for x in self.testFeatures]
        # print self.trainFeatures
        # print x
        # print y

        predicthome = [0, 0, 0]
        predictdraw = [0, 0, 0]
        predictaway = [0, 0, 0]

        clf = svm.SVC(kernel='rbf')
        clf.decision_function_shape = 'ovr'

        right = 0

        for temp in enumerate(tx):
            flag = 0
            clf.fit(x, y)

            detailResult = [self.testSet[temp[0]][2], self.testSet[temp[0]][3], self.testSet[temp[0]][6]]
            if (ty[temp[0]] == 1):
                if (clf.predict(temp[1])[0] == 1):
                    detailResult.append('H')
                    right += 1
                    flag = 1
                    predicthome[0] += 1
                elif (clf.predict(temp[1])[0] == 0):
                    detailResult.append('D')
                    predicthome[1] += 1
                else:
                    detailResult.append('A')
                    predicthome[2] += 1
            elif (ty[temp[0]] == 0):
                if (clf.predict(temp[1])[0] == 1):
                    detailResult.append('H')
                    predictdraw[0] += 1
                elif (clf.predict(temp[1])[0] == 0):
                    detailResult.append('D')
                    right += 1
                    flag = 1
                    predictdraw[1] += 1
                else:
                    detailResult.append('A')
                    predictdraw[2] += 1
            else:
                if (clf.predict(temp[1])[0] == 1):
                    detailResult.append('H')
                    predictaway[0] += 1
                elif (clf.predict(temp[1])[0] == 0):
                    detailResult.append('D')
                    predictaway[1] += 1
                else:
                    detailResult.append('A')
                    right += 1
                    flag = 1
                    predictaway[2] += 1
            detailResults.append(detailResult)

            if (flag == 0):
                ##update training set
                newTrainEx = self.getFeaturesOfSingleGame(self.testSet[temp[0]][2], self.testSet[temp[0]][3],
                                                          self.testSet[temp[0]][1], self.testSet[temp[0]][6], 'E2015')
                print(newTrainEx)
                x.append(newTrainEx[1:])
                y.append(newTrainEx[0])

        print(float(right) / len(tx))
        print(detailResults)
        print(predicthome, predictdraw, predictaway)


gameP = GamePredictor()
gameP.doSVMOnline()
