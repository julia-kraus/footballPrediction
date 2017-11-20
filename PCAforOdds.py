import extract_data
from sklearn.decomposition import PCA

season = 'E2015'


class PCAForTeamPerformance():
    def __init__(self):
        self.dataset = extract_data.FootballData().dataSets[season]
        self.oddsSet = []

    def extractPerformanceData(self):
        self.oddsSet = [x[11:21:2] for x in self.dataset]
        print(self.oddsSet)

    def runPCA(self):
        pca = PCA(n_components=5)
        pca.fit(self.oddsSet)
        print(pca.explained_variance_ratio_)


pca = PCAForTeamPerformance()
pca.extractPerformanceData()
pca.runPCA()
