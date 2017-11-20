from sklearn.cluster import KMeans
from extract_data import FootballData
from sklearn import preprocessing
import numpy as np

fileName = 'D2015'

numbersOfCluster = 5


class clusterTeams:
    def __init__(self):

        self.team_features = []
        self.data_set = []
        self.data_set2 = []
        self.centers = []
        self.prediction = []
        self.teams = [[[0 for col2 in range(3)] for col in range(5)] for row in range(5)]
        self.teams_cluster = {}
        self.scores = []
        self.fbData = FootballData()
        self.team_names = self.fbData.teamNamesPerSeason[fileName]

    def readFile(self, fileName):

        tempDataSet = self.fbData.seasons_data[fileName]
        return tempDataSet

    def storeGameResultForEachCluster(self, team1, team2, result):

        if team1 in list(self.teams_cluster.keys()):
            if team2 in list(self.teams_cluster.keys()):
                if (result == 'H'):
                    self.teams[self.teams_cluster[team1] - 1][self.teams_cluster[team2] - 1][0] += 1
                    self.teams[self.teams_cluster[team2] - 1][self.teams_cluster[team1] - 1][2] += 1
                elif (result == 'D'):
                    self.teams[self.teams_cluster[team1] - 1][self.teams_cluster[team2] - 1][1] += 1
                    self.teams[self.teams_cluster[team2] - 1][self.teams_cluster[team1] - 1][1] += 1
                elif (result == 'A'):
                    self.teams[self.teams_cluster[team1] - 1][self.teams_cluster[team2] - 1][2] += 1
                    self.teams[self.teams_cluster[team2] - 1][self.teams_cluster[team1] - 1][0] += 1
                else:
                    print()

    def fillTheEmptyData(self, fileName):

        self.readFile(fileName, self.data_set2)

        print(self.data_set2)

    def transformResultToScore(self, result):

        if ((result[0] + result[1] + result[2]) != 0):
            return float((result[0] * 3 + result[1])) / (result[0] + result[1] + result[2])
        else:
            return 0.

    def extractFeatures(self):
        count = 0
        for names in self.team_names:
            features = [0, 0, 0, 0, 0]
            for temp in self.data_set:
                if temp[2] == names:
                    for i in range(11, 20, 2):
                        features[int(i) % 11 / 2] = features[int(i) % 11 / 2] + int(temp[i])
                if temp[3] == names:
                    for i in range(12, 20, 2):
                        features[int(i) % 12 / 2] = features[int(i) % 12 / 2] + int(temp[i])
            self.team_features.append(features)

    def clustering(self, K):

        km = KMeans(n_clusters=K)

        print(self.team_features)
        scale_features = preprocessing.scale(np.array(self.team_features, dtype=float))
        # preprocessing.normalize(np.array(self.team_features), norm='l2')
        print(scale_features)
        km.fit(scale_features)

        self.centers = km.cluster_centers_
        # self.centers[self.centers<0] = 0 #the minimization function may find very small negative numbers, we threshold them to 0
        self.centers = self.centers.round(2)

        print('\n--------Centers of the four different clusters--------')
        print('Deal\t Cent1\t Cent2\t Cent3\t Cent4 \t Cent5')

        for i in range(5):
            print((i + 1, '\t', self.centers[0, i], '\t', self.centers[1, i], '\t', self.centers[2, i], '\t',
                   self.centers[3, i], '\t', self.centers[4, i]))

        self.prediction = km.predict(scale_features)

        print('\n--------Which cluster each customer is in--------')
        print(('{:<15}\t{}'.format('Customer', 'Cluster')))

        for i in range(len(self.prediction)):
            print(('{:<15}\t{}'.format(self.team_names[i], self.prediction[i] + 1)))

        for i in range(len(self.team_names)):
            self.teams_cluster[self.team_names[i]] = self.prediction[i] + 1

    def run(self, fileName, K):

        # read file
        self.data_set = self.readFile(fileName, self.data_set)

        # extractFeature
        self.extractFeatures()

        # run clustering
        self.clustering(K)

        for line in self.data_set:
            self.storeGameResultForEachCluster(line[2], line[3], line[6])
        for team in self.teams:
            temp = [self.transformResultToScore(x) for x in team]
            self.scores.append(temp)


teamCluster = clusterTeams()

teamCluster.run(fileName, numbersOfCluster)
print(teamCluster.team_features)
# teamCluster.fillTheEmptyData(fileName2)
# teamCluster.readFile2(fileName)

print(teamCluster.teams_cluster)
print(teamCluster.teams)
print(teamCluster.scores)
# print team_features
# print count
