from extract_data import FootballData
import extract_data as pd

# Number of past games to be considered
K = 6


class PastKGames:
    """docstring for PastKGames"""

    def __init__(self, season):
        self.trainSet = []
        self.fbData = FootballData()
        self.season = season

        self.set_trainData()

    def set_trainData(self):

        self.trainSet = self.fbData.dataSets['D2015']
        self.trainSet.extend(self.fbData.dataSets[self.season])
        self.trainSet.extend(self.fbData.dataSets['D2013'])
        self.trainSet.extend(self.fbData.dataSets['D2013'])

    def find_kth_winning_pre(self, team, gamedate, game_num):
        k = 0
        full_time_result = []  # full time result
        for item in self.trainSet:
            if pd.compare_datetime(gamedate, item[1]):  # compare the date
                if item[2] == team:
                    k = k + 1
                    if item[6] == 'H':
                        full_time_result.append(3)
                    elif item[6] == 'A':
                        full_time_result.append(1)
                    else:
                        full_time_result.append(2)
                if item[3] == team:
                    k = k + 1
                    if item[6] == 'A':
                        full_time_result.append(3)
                    elif item[6] == 'H':
                        full_time_result.append(1)
                    else:
                        full_time_result.append(2)
                if k >= game_num:
                    return full_time_result
        return None

    def getTwoTeamPastKGameResults(self, hometeam, awayteam, date, K):

        twoTeamPastKGameResults = {}

        twoTeamPastKGameResults[hometeam] = self.find_kth_winning_pre(hometeam, date, K)

        twoTeamPastKGameResults[awayteam] = self.find_kth_winning_pre(awayteam, date, K)

        return twoTeamPastKGameResults

    def getTwoTeamPastAvgKGameResults(self, hometeam, awayteam, date, K):

        twoTeamPastKGameAvgResults = self.getTwoTeamPastKGameResults(hometeam, awayteam, date, K)

        twoTeamPastKGameAvgResults[hometeam] = float(sum(twoTeamPastKGameAvgResults[hometeam])) / len(
            twoTeamPastKGameAvgResults[hometeam])

        twoTeamPastKGameAvgResults[awayteam] = float(sum(twoTeamPastKGameAvgResults[awayteam])) / len(
            twoTeamPastKGameAvgResults[awayteam])

        return twoTeamPastKGameAvgResults


class gamePastKHistory():
    def __init__(self):

        self.history = []
        self.fbData = FootballData()
        self.feature = []
        self.trainData = self.fbData.dataSets['D2015']
        self.trainData.extend(self.fbData.dataSets['D2014'])

    # add all data



    def findHistoryPastKBetweenTwoTeams(self, hometeam, awayteam, date, K):

        final_result = {hometeam: [], awayteam: []}

        def add_result(hometeam, awayteam, x):
            if (x[1] == 'H'):
                final_result[hometeam].append(3)
                final_result[awayteam].append(0)
            elif (x[1] == 'D'):
                final_result[hometeam].append(1)
                final_result[awayteam].append(1)
            else:
                final_result[hometeam].append(0)
                final_result[awayteam].append(3)

        def findH(x):
            # compare the date, hometeam and awayteam
            if (pd.compare_datetime(date, x[1]) and hometeam == x[2] and awayteam == x[3]):
                return ('+', x[6])
            elif (pd.compare_datetime(date, x[1]) and hometeam == x[3] and awayteam == x[2]):
                return ('-', x[6])

        def addHistoryResult(x):

            if (x[0] == '+'):
                add_result(hometeam, awayteam, x)
            elif (x[0] == '-'):
                add_result(awayteam, hometeam, x)

        # for data in self.fbData().dataSets.values():
        resultList = [list(map(findH, self.fbData.dataSets[x.split('.')[0]])) for x in self.fbData.filenames[0:K]]

        resultList = [[x for x in result if x != None] for result in resultList]

        list(map(lambda result: list(map(addHistoryResult, result)), resultList))

        return final_result

    def findAvgHistoryPastKBetweenTwoTeams(self, hometeam, awayteam, date, K):

        avgResults = {}

        avgResults = self.findHistoryPastKBetweenTwoTeams(hometeam, awayteam, date, K)
        # print avgResults
        if len(avgResults[hometeam]) == 0:
            avgResults[hometeam] = 1

            avgResults[awayteam] = 1
        else:
            avgResults[hometeam] = float(sum(avgResults[hometeam])) / len(avgResults[hometeam])

            avgResults[awayteam] = float(sum(avgResults[awayteam])) / len(avgResults[awayteam])

        return avgResults


class pastKGamePerform():
    def __init__(self, season):
        self.fbData = FootballData().dataSets['D2015']
        self.fbData.extend(FootballData().dataSets[season])
        self.fbData.extend(FootballData().dataSets['D2013'])
        self.performance = []

    def find_K_Performance(self, team, game_date, feature, K):
        # already does cases for home and away team!
        # -->feature goals [4], feature corners [16], feature shots on target [12]
        k = 0
        full_time_result = []  # full time result
        for item in self.fbData:
            if pd.compare_datetime(game_date, item[1]):  # compare the date if it was previous game
                if item[2] == team:
                    k += 1
                    full_time_result.append(int(item[feature]))
                if item[3] == team:
                    k = k + 1
                    full_time_result.append(int(item[feature + 1]))
                if k >= K:
                    return full_time_result
        return None

    # Performance for one feature. Features used here are: goals[4,5]: FTHG, FTAG,
    # corners[16,17]: HC, AC, shots on target[12,13]: HST, AST
    def getPerformance(self, hometeam, awayteam, gameDate, feature, K):

        twoTeamPastKGamePer = {}

        twoTeamPastKGamePer[hometeam] = self.find_K_Performance(hometeam, gameDate, feature, K)

        twoTeamPastKGamePer[awayteam] = self.find_K_Performance(awayteam, gameDate, feature, K)

        return twoTeamPastKGamePer

    def getAvgPerformance(self, hometeam, awayteam, gameDate, feature, K):

        twoTeamPastKPer = self.getPerformance(hometeam, awayteam, gameDate, feature, K)

        twoTeamPastKPer[hometeam] = float(sum(twoTeamPastKPer[hometeam])) / len(twoTeamPastKPer[hometeam])
        twoTeamPastKPer[awayteam] = float(sum(twoTeamPastKPer[awayteam])) / len(twoTeamPastKPer[awayteam])
        return twoTeamPastKPer


# a = gamePastKHistory()

# pg = pastKGamePerform('D2014')
# perDict = pg.getAvgPerformance("Dortmund", "Hannover", "25/10/14", 13, 4)
# print(perDict["Dortmund"])
# print(perDict["Hannover"])

# perDict = pg.getAvgPerformance("Chelsea","Bournemouth","07/12/15",13,6)
# print perDict["Chelsea"]
# print perDict["Bournemouth"]

# perDict = pg.getAvgPerformance("Chelsea","Bournemouth","07/12/15",15,6)
# print perDict["Chelsea"]
# print perDict["Bournemouth"]

# perDict = pg.getAvgPerformance("Chelsea","Bournemouth","07/12/15",17,6)
# print perDict["Chelsea"]
# print perDict["Bournemouth"]

pastKgame = PastKGames('D2015')

pastResult = pastKgame.getTwoTeamPastKGameResults("Hamburg", "Darmstadt", "09/04/16", 4)
print('hometeam:', pastResult["Hamburg"])
print('awayteam:', pastResult["Darmstadt"])
# g = gamePastKHistory()
# print g.findHistoryPastKBetweenTwoTeams('Chelsea','Bournemouth',"07/12/15",9)
# print pastKgame.trainSet[3][6]
